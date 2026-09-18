from fastapi import Depends
from app.infrastructure.llm.client import get_llm_client
from openai import OpenAI

#This file contains the Dependency P

def get_message() -> str:
    return "Hello from Dependency."

# @router.get("/test")
# def test(message: str = Depends(get_message)):
#     return {
#         "message": message
#     }

def provide_llm_client() -> OpenAI: # This function exposes dependency provided/created by get_llm_client()
    return get_llm_client()
