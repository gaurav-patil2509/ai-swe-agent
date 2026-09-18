from openai import OpenAI
from app.domain.ports.llm import LLM

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
        