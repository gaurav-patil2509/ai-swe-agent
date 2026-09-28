import json
from openai import OpenAI
from app.domain.ports.llm import LLM
from app.domain.entities.agent import AgentResponse, ToolCall

class OpenRouterLLM:

    def __init__(self, client: OpenAI, model: str):
        self.client=client
        self.model= model

    def generate(self, message:str)->str:
        response = self.client.responses.create(
            model= self.model,
            input = message,
        )
        return response.output_text

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
    
        print("\n============RAW RESPONSE=============")
        print(response)
        print("======================================")
    
        tool_calls = []
    
        for item in response.output:
    
            print("OUTPUT ITEM:", item)
            print("ITEM TYPE:", item.type)
    
            if item.type == "function_call":
                print("FOUND FUNCTION CALL!")
    
                arguments = json.loads(item.arguments)
    
                tool_calls.append(
                    ToolCall(
                        name=item.name,
                        arguments=arguments,
                    )
                )
    
        print("PARSED TOOL CALLS:", tool_calls)
    
        if tool_calls:
            return AgentResponse(tool_calls=tool_calls)
    
        return AgentResponse(content=response.output_text)