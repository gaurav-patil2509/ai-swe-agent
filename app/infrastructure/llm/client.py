"""
OpenAI client configuration.

This module creates a single reusable OpenAI client for the application.
It does not make API calls.
"""

from openai import OpenAI
from app.core.config import settings
from app.core.logging import get_logger

logger= get_logger(__name__)
logger.info("Initializing LLM Client(base_url=%s)", settings.llm_base_url)

def get_llm_client() -> OpenAI:  # -> OpenAI is the type hint that this function returns the OpenAI() object 
    return OpenAI( 
    api_key=settings.llm_api_key,
    base_url= settings.llm_base_url
    )

logger.info("LLM Client Intialized Successfully.")
