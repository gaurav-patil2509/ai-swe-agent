from typing import Protocol

class LLM(Protocol):

    def generate(self, message:str)->str:
        ...
