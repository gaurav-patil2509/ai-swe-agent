from dataclasses import dataclass
from typing import Any

@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]
    call_id : str

@dataclass
class AgentResponse:
    content: str | None = None
    tool_calls: list[ToolCall] | None = None
    raw_response: Any | None = None