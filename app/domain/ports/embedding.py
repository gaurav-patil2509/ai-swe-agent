from typing import Protocol

class Embedding(Protocol):
    def embed(self, text:str)-> list[float]:
        ...