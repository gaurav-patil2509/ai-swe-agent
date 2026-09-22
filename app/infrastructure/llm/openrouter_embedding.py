from openai import OpenAI

from app.domain.ports.embedding import Embedding

class OpenRouterEmbedding:
    def __init__(self, client: OpenAI, model:str):
        self.client= client
        self.model= model

    def embed(self, text:str)-> list[float]:
        response= self.client.embeddings.create(
            model= self.model, 
            input=text,
        )
        return response.data[0].embedding
        