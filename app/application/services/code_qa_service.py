from app.domain.ports.llm import LLM
from app.application.services.code_retrieval_service import CodeRetrieval
from app.application.services.context_builder import ContextBuilder

class CodeQAService:

    def __init__(self, llm: LLM, retrieval_service: CodeRetrieval, context_builder: ContextBuilder):
        self.llm= llm
        self.retrieval_service = retrieval_service
        self.context_builder = context_builder

    def answer(
            self,
            question: str,
            top_k: int = 5
    )->str:
        
        chunks = self.retrieval_service.retrieve(
            query= question,
            top_k= top_k
        )

        context = self.context_builder.build(chunks)

        prompt = f"""
You are an AI software engineering assistant.
 
Answer the user's question using the provided codebase context.
 
Rules:
Base your answer primarily on the provided code.
Do not invent files, classes, functions, or behavior that are not supported by the context.
If the provided context is insufficient, say that the relevant code was not found.
Mention relevant file paths and line ranges when useful.
 
CODEBASE CONTEXT:
 
{context}
 
USER QUESTION:
 
{question}
"""
 
        return self.llm.generate(prompt)

        
