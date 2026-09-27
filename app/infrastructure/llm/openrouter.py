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
            tools: list[dict]
    )-> AgentResponse:

        response = self.client.responses.create(
             model= self.model,
             input= message, 
             tools = tools, 
             tool_choice= "auto"
        )

        tool_calls= []

        for item in response.output:
            if item.type == "function_call":

                arguments = json.loads(item.arguments)

                tool_calls.append{
                    ToolCall(
                        name= item.name,
                        arguments= arguments,
                    )
                }    

            if tool_calls:
                return AgentResponse(
                    tool_calls= tool_calls
                )   
            return AgentResponse(
                content= response.output_text
            )