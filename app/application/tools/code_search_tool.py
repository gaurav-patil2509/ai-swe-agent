from app.application.services.code_retrieval_service import CodeRetrieval
from app.application.services.context_builder import ContextBuilder

class CodeSearchTool:

    name= "search_code"

    description= (
        "Search the codebase for code relevant to a given question "
        "and return the most relevant code sections."
    )

    def __init__(self, retrieval_service: CodeRetrieval, context_builder: ContextBuilder):
        self.retrieval_service= retrieval_service
        self.context_builder= context_builder

    def execute(
            self, 
            query: str,
            top_k: int = 5
    )-> str:
        chunks = self.retrieval_service.retrieve(
            query= query,
            top_k=top_k
        )

        return self.context_builder.build(chunks)
        