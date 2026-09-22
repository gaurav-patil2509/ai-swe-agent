from app.domain.entities.code import CodeChunk

class CodeChunker:
    def __init__(self, chunk_size: int=40, overlap: int= 5):
        self.chunk_size= chunk_size
        self.overlap= overlap
   
    
    def chunk_file(self, content:str, file_path:str)->list[CodeChunk]:
        lines= content.splitlines()
        chunks = []
        start =0

        while start < len(lines):
            end = min(start+self.chunk_size, len(lines))

            chunk_content = "\n".join(lines[start:end])

            chunks.append(
                CodeChunk(
                    content= chunk_content,
                    file_path= file_path,
                    start_line= start+1,
                    end_line= end,
                )
            )

            if end == len(lines):
                break

            start = end- self.overlap
            
        return chunks