import json

from openai import OpenAI

from app.domain.ports.llm import LLM
from app.domain.entities.agent import AgentResponse, ToolCall


class OpenRouterLLM:

    def __init__(self, client: OpenAI, model: str):
        self.client = client
        self.model = model

    def generate(self, message: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=message,
        )

        return response.output_text

    def _parse_response(self, response) -> AgentResponse:
        tool_calls = []

        for item in response.output:

            if item.type == "function_call":

                tool_calls.append(
                    ToolCall(
                        name=item.name,
                        arguments=json.loads(item.arguments),
                        call_id=item.call_id,
                    )
                )

        return AgentResponse(
            content=response.output_text or None,
            tool_calls=tool_calls or None,
            raw_response=response,
        )

    def generate_with_tools(
        self,
        message: str,
        tools: list[dict],
    ) -> AgentResponse:

        response = self.client.responses.create(
            model=self.model,
            input=message,
            tools=tools,
            tool_choice="auto",
        )

        return self._parse_response(response)

    
    def continue_with_tools(
        self,
        input_items: list[dict],
        tools: list[dict],
    ) -> AgentResponse:

        response = self.client.responses.create(
            model=self.model,
            input=input_items,
            tools=tools,
            tool_choice="auto",
        )

        return self._parse_response(response)
