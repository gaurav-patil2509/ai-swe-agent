import json

from app.domain.ports.llm import LLM
from app.application.tools.tool_definition import to_openai_tool
from app.application.tools.tool_registry import ToolRegistry


class CodeAgent:

    def __init__(
        self,
        llm: LLM,
        tool_registry: ToolRegistry
    ):
        self.llm = llm
        self.tool_registry = tool_registry

    def run(self, task: str) -> str:

        registered_tools = self.tool_registry.all()

        tools = [
            to_openai_tool(tool)
            for tool in registered_tools
        ]

        # 1. Maintain conversation history locally
        conversation_history = [
            {
                "role": "user",
                "content": task,
            }
        ]

        # 2. First LLM request
        response = self.llm.generate_with_tools(
            message=task,
            tools=tools,
        )

        max_iterations = 5

        for iteration in range(max_iterations + 1):

            # 3. If no tool calls, return final answer
            if not response.tool_calls:
                return response.content or ""

            if iteration == max_iterations:
                break

            # 4. Preserve ALL assistant output items.
            # This includes function calls and reasoning items.
            for item in response.raw_response.output:

                if hasattr(item, "model_dump"):
                    item = item.model_dump(exclude_none=True)

                conversation_history.append(item)

            tool_outputs = []

            # 5. Execute requested tools
            for tool_call in response.tool_calls:

                tool = self.tool_registry.get(tool_call.name)

                if tool is None:
                    result = f"Error: Tool '{tool_call.name}' not found."

                else:
                    try:
                        result = tool.execute(
                            **tool_call.arguments
                        )

                    except Exception as exc:
                        result = f"Tool execution failed: {str(exc)}"

                if not isinstance(result, str):
                    result = json.dumps(result, default=str)

                tool_outputs.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": result,
                })

            # 6. Add tool results to conversation history
            conversation_history.extend(tool_outputs)

            # 7. Ask LLM again with COMPLETE history
            response = self.llm.continue_with_tools(
                input_items=conversation_history,
                tools=tools,
            )

        return "Agent stopped: maximum tool-call iterations reached."
