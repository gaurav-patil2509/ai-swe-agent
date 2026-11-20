
from typing import Protocol

from app.domain.entities.agent import AgentResponse


class LLM(Protocol):

    def generate(self, message: str) -> str:
        ...

    def generate_with_tools(
        self,
        message: str,
        tools: list[dict]
    ) -> AgentResponse:
        ...

    def continue_with_tools(
        self,
        input_items: list[dict],
        tools: list[dict]
    ) -> AgentResponse:
        ...
