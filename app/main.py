"""
Application entrypoint.

We use an "app factory" function rather than a bare module-level `app = FastAPI()`
so that tests can create fresh, isolated app instances if ever needed
(e.g. with different settings/overrides).
"""

from fastapi import FastAPI

from app.api.v1 import health
from app.api.v1 import chat
from app.core.config import settings
from app.core.logging import configure_logging, get_logger

configure_logging()
logger = get_logger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description= "AI Software Engineering Agent Backend"
    )

    app.include_router(health.router, prefix="/api/v1") 
    app.include_router(chat.router, prefix="/api/v1")
    
    logger.info("Application configured (env=%s)", settings.environment)
    return app


app = create_app()
