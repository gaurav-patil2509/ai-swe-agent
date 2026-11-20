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

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    app_name: str = "ai-swe-agent"
    environment: str = "development"
    log_level: str = "INFO"

    # LLM (OpenAI-compatible)
    llm_api_key: str
    llm_base_url: str = "https://openrouter.ai/api/v1"
    llm_model: str = "gpt-4o-mini"

    # Embedding model
    embedding_model: str = "openai/text-embedding-3-small"
    codebase_path: str = "."
    # ChromaDB
    chroma_persist_dir: str = "./data/chroma"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

