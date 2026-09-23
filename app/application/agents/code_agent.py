from app.application.tools.code_search_tool import CodeSearchTool
from app.domain.ports.llm import LLM

class CodeAgent:

    def __init__(self, llm: LLM, code_search_tool: CodeSearchTool):
        self.llm = llm
        self.code_search_tool = code_search_tool

    def run(self, task: str)-> str:
        context = self.code_search_tool.execute(
            query=task, 
            top_k= 5
        )
        prompt = f"""
You are an AI software engineering agent.
 
Answer the user's question using the provided codebase context.
 
CODEBASE CONTEXT:
 
{context}
 
USER TASK:
 
{task}
 
Rules:
Base your answer on the provided code.
Do not invent implementation details.
Mention relevant files and line ranges when useful.
If the context is insufficient, clearly say so.
"""
 
        return self.llm.generate(prompt)