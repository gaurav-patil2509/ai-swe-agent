
from fastapi import Depends
from openai import OpenAI

from app.infrastructure.llm.client import (
    get_llm_client as create_llm_client
)


def get_message() -> str:
    return "Hello from Dependency."


def get_llm_client() -> OpenAI:
    """
    FastAPI dependency that provides the configured LLM client.
    """
    return create_llm_client()
