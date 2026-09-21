from typing import Protocol

class CodeRepository(Protocol):

    def list_files(self)->list[str]:
        ...

    def read_files(self, path: str)-> str:
        ...
        