from fastapi import APIRouter, Depends
from openai import OpenAI

from app.application.services.chat_service import ChatService
from app.core.config import settings
from app.api.deps import get_llm_client
from app.domain.entities.chat import ChatRequest, ChatResponse

router = APIRouter(
    prefix="/chat",
    tags= ["chat"],
)

def get_chat_service(
        client: OpenAI = Depends(get_llm_client), 
    )->ChatService:
    return ChatService(
        client=client,
        model= settings.llm_model
    )

@router.post("", response_model=ChatResponse)
def chat( request: ChatRequest, 
         service: ChatService = Depends(get_chat_service), 
         ): 
       answer = service.chat(request.message)
       return ChatResponse(answer=answer)