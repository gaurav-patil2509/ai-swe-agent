from typing import Protocol

class Agent(Protocol):

    def run(self, task: str)->str:
        ...

        