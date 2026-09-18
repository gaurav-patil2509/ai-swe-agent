"""
Logging setup.

We use stdlib `logging` (no extra dependency needed for this) configured to
emit structured, timestamped lines. In production this format is easy to
ship to any log aggregator (Datadog, CloudWatch, etc.) as-is, or swapped
for JSON output later by changing only this file.
"""

import logging
import sys

from app.core.config import settings


def configure_logging() -> None:
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)

    # Avoid duplicate handlers if configure_logging() is called more than once
    # (e.g. in tests that create the app multiple times).
    if root_logger.handlers:
        return

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
