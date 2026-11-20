
"""
OpenAI-compatible client configuration.

Creates a reusable client configured for the selected LLM provider.
"""

from openai import OpenAI

from app.core.config import get_settings
from app.core.logging import get_logger

logger = get_logger(__name__)


def get_llm_client() -> OpenAI:
    settings = get_settings()

    logger.info(
        "Initializing LLM Client (base_url=%s)",
        settings.llm_base_url
    )

    client = OpenAI(
        api_key=settings.llm_api_key,
        base_url=settings.llm_base_url
    )

    logger.info(
        "LLM Client initialized successfully (base_url=%s)",
        client.base_url
    )

    return client
