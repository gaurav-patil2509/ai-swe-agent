import chromadb
 
from app.domain.entities.code import CodeChunk
from app.domain.ports.vector_store import VectorStore
 
 
class ChromaVectorStore:
 
    def __init__(self, persist_dir: str):
        self.client = chromadb.PersistentClient(
            path=persist_dir
        )
 
        self.collection = self.client.get_or_create_collection(
            name="codebase"
        )
 
    def add(
        self,
        chunks: list[CodeChunk],
        embeddings: list[list[float]],
    ) -> None:
 
        ids = [
            f"{chunk.file_path}:{chunk.start_line}-{chunk.end_line}"
            for chunk in chunks
        ]
 
        documents = [
            chunk.content
            for chunk in chunks
        ]
 
        metadatas = [
            {
                "file_path": chunk.file_path,
                "start_line": chunk.start_line,
                "end_line": chunk.end_line,
            }
            for chunk in chunks
        ]
        #Putting Data into ChromaDB (this will add record if it doesn't exist otherwise update it) 
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )
 
    def search(
        self,
        embedding: list[float],
        top_k: int = 5,
    ) -> list[CodeChunk]:
 
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )
 
        chunks = []
 
        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
 
        for document, metadata in zip(documents, metadatas):
            chunks.append(
                CodeChunk(
                    content=document,
                    file_path=metadata["file_path"],
                    start_line=metadata["start_line"],
                    end_line=metadata["end_line"],
                )
            )
 
        return chunks