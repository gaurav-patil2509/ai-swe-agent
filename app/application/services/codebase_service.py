from app.application.services.code_chunker import CodeChunker
from app.domain.entities.code import CodeChunk
from app.domain.ports.code_repository import CodeRepository

class CodebaseService:
    def __init__(self, repository:CodeRepository, chunker: CodeChunker):
        self.repository= repository
        self.chunker = chunker

    def chunk_codebase(self)-> list[CodeChunk]:
        chunks = []
        files = self.repository.list_files()

        for file_path in files:
            content = self.repository.read_files(file_path)

            file_chunks = self.chunker.chunk_file(
                content= content,
                file_path= file_path,
            )

            chunks.extend(file_chunks)

        return chunks

    

        