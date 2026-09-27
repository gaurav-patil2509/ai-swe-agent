from dataclasses import dataclass
from typing import Any

@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]

@dataclass
class AgentResponse:
    content: str | None = None
    tool_calls: ToolCall | None = None