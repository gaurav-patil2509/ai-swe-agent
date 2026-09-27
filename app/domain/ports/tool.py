from typing import Protocol

class Tool:
    @property
    def name(self)->str:
        ...

    def description(self)->str:
        ...

    def parameters(self)->dict[str, Any]:
        ...

    def execute(self, **kwargs: Any)->str:
        ...