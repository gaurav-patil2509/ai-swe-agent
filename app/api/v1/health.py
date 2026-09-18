from fastapi import APIRouter
# from pydantic import BaseModel

# from app.core.config import settings

# router = APIRouter(tags=["health"])


# class HealthResponse(BaseModel):
#     status: str
#     app_name: str
#     environment: str


# @router.get("/health", response_model=HealthResponse)
# def health_check() -> HealthResponse:
#     return HealthResponse(
#         status="ok",
#         app_name=settings.app_name,
#         environment=settings.environment,
#     )
from fastapi import FastAPI
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.config import settings
from app.api.deps import get_message
from app.api.deps import get_llm_client
from openai import OpenAI




# app = FastAPI()
router = APIRouter(
    tags= ["Health"]
)

class HealthResponse(BaseModel):
    status: str
    app_name: str
    enviroment: str
    

@router.get("/health",
             response_model= HealthResponse
             )
def health() -> HealthResponse: #return type hint
    return HealthResponse(
        status="ok",
        app_name= settings.app_name,
        enviroment= settings.environment
    )

# @router.get("/test")
# def dependency_test(message: str = Depends(get_message)):
#     return {
#         "message": message
#     }
@router.get("/test")
def dependency_test(
    client: OpenAI = Depends(get_llm_client), 
):
    return {
        "Client created": client is not None
    }