from typing import Protocol

class Tool:
    @property
    def name(self)->str:
        ...

    def description(self)->str:
        ...
        
    def execute(self, **kwargs)->str:
        ...