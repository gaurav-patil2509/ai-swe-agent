from app.domain.ports.embedding import Embedding
from app.domain.ports.vector_store import VectorStore
from app.domain.entities.code import CodeChunk


class CodeRetrieval:

    def __init__(self, embedding : Embedding, vector_store: VectorStore):
        self.embedding = embedding
        self.vector_store =  vector_store

    def retrieve(
            self, 
            query: str,
            top_k: int=5
    )-> list[CodeChunk]:

        query_embedding = self.embedding.embed(query)
        return self.vector_store.search(
            embedding=query_embedding,
            top_k= top_k
        )