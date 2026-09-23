from app.domain.entities.code import CodeChunk

class ContextBuilder:

    def build(
            self, 
            chunks: list[CodeChunk]
    )->str:
        sections=[]

        for chunk in chunks:
            section = (
                f"File path: {chunk.file_path}\n"
                f"Lines: {chunk.start_line}-{chunk.end_line}\n"
                f"```Text\n"
                f"{chunk.content}\n"
                f"```"
            )

            sections.append(section)

        return "\n\n".join(sections)