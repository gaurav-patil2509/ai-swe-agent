from typing import Protocol
from app.domain.entities.code import CodeChunk

class VectorStore:

    def search(self, embedding: list[float], top_k: int = 5) -> list[CodeChunk]: #find chunks similar to a query vector 
        ...

    def add(self, chunks: list[CodeChunk], embedding: list[list[float]]) -> None:  # Store Code chunks + their vectors
        ...