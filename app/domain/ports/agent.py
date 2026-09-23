from typing import Protocol

class Agent:

    def run(self, task: str)->str:
        ...

        