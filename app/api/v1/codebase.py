from fastapi import APIRouter, Depends
from openai import OpenAI
 
from app.api.deps import get_llm_client
from app.application.services.code_qa_service import CodeQAService
from app.application.services.code_retrieval_service import CodeRetrieval
from app.application.services.context_builder import ContextBuilder
from app.core.config import settings
from app.domain.entities.chat import ChatRequest, ChatResponse
from app.infrastructure.llm.openrouter import OpenRouterLLM
from app.infrastructure.llm.openrouter_embedding import OpenRouterEmbedding
from app.infrastructure.vectorstore.chroma import ChromaVectorStore
from app.application.tools.code_search_tool import CodeSearchTool
from app.application.agents.code_agent import CodeAgent
 
router = APIRouter(
    prefix="/codebase",
    tags=["codebase"],
)

def get_code_agent(
    client: OpenAI = Depends(get_llm_client),
) -> CodeAgent:
 
    llm = OpenRouterLLM(
        client=client,
        model=settings.llm_model,
    )
 
    embedding = OpenRouterEmbedding(
        client=client,
        model=settings.embedding_model,
    )
 
    vector_store = ChromaVectorStore(
        persist_dir=settings.chroma_persist_dir,
    )
 
    retrieval_service = CodeRetrieval(
        embedding=embedding,
        vector_store=vector_store,
    )
 
    context_builder = ContextBuilder()

    code_search_tool = CodeSearchTool(
        retrieval_service= retrieval_service,
        context_builder= context_builder
    )
 
    return CodeAgent(
        llm= llm,
        code_search_tool= code_search_tool
    )
 
def get_code_qa_service(
    client: OpenAI = Depends(get_llm_client),
) -> CodeQAService:
 
    llm = OpenRouterLLM(
        client=client,
        model=settings.llm_model,
    )
 
    embedding = OpenRouterEmbedding(
        client=client,
        model=settings.embedding_model,
    )
 
    vector_store = ChromaVectorStore(
        persist_dir=settings.chroma_persist_dir,
    )
 
    retrieval_service = CodeRetrieval(
        embedding=embedding,
        vector_store=vector_store,
    )
 
    context_builder = ContextBuilder()
 
    return CodeQAService(
        llm=llm,
        retrieval_service=retrieval_service,
        context_builder=context_builder,
    )
 
 
@router.post("/ask", response_model=ChatResponse)
def ask_codebase(
    request: ChatRequest,
    service: CodeQAService = Depends(get_code_qa_service),
):
    answer = service.answer(request.message)
 
    return ChatResponse(answer=answer)

@router.post("/agent", response_model= ChatResponse)
def code_agent(
    request: ChatRequest,
    agent: CodeAgent = Depends(get_code_agent)
):
    answer= agent.run(request.message)

    return ChatResponse(answer=answer)