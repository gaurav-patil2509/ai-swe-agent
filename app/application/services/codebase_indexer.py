from app.domain.ports.code_repository import CodeRepository
from app.domain.ports.vector_store import VectorStore
from app.application.services.code_chunker import CodeChunker
from app.domain.ports.embedding import Embedding

class CodebaseIndexer:

    def __init__(self, repository: CodeRepository, chunker: CodeChunker, embedding:Embedding,  vector_store: VectorStore ):
        self.repository= repository
        self.chunker = chunker
        self.embedding = embedding
        self.vector_store = vector_store

    def index(self)->int:
        all_chunks = []

        files = self.repository.list_files()

        for file_path in files:
            content = self.repository.read_files(file_path)
            chunks = self.chunker.chunk_file(
                content= content,
                file_path=file_path
            )
            all_chunks.extend(chunks)

        #This below code is the abbrevation of this     
        # embeddings = []
        # for chunk  in all_chunks:
        #     vector= self.embedding.embed(chunk.content)
        #     embeddings.append(vector)

 
        embeddings = [
            self.embedding.embed(chunk.content)
            for chunk in all_chunks
        ]

        self.vector_store.add(
            chunks= all_chunks, 
            embeddings= embeddings
        )

        return len(all_chunks)





        