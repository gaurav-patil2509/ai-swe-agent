"""
Centralized, typed configuration.

Why this exists instead of scattered os.getenv() calls:
- Validated once, at startup — a missing/invalid required var fails fast
  with a clear error, instead of blowing up mid-request three layers deep.
- Typed — editors/tools know LOG_LEVEL is a str, not "something from the env".
- Single source of truth — every other module imports `settings` from here
  instead of reading the environment directly.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "ai-swe-agent"
    environment: str = "development"
    log_level: str = "INFO"
   

    # LLM (OpenAI-compatible)
    llm_api_key: str = "sk-placeholder"
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"

    #Embedding model
    embedding_model: str = "openai/text-embedding-3-small"

    # ChromaDB
    chroma_persist_dir: str = "./data/chroma"


@lru_cache
def get_settings() -> Settings:
    """
    Cached so we parse/validate the environment exactly once per process.
    This is the function we'll inject via FastAPI's Depends() later —
    that's the dependency-injection seam for config.
    """
    return Settings()


settings = get_settings()
