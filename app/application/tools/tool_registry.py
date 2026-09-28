from app.domain.ports.tool import Tool


class ToolRegistry:

    def __init__(self, tools: list[Tool]):
        self.tools= {
            tool.name: tool
            for tool in tools
        }

    def get(self, name: str)-> Tool:
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")
        return self.tools[name]

    def all(self)-> list[Tool]:
        return list(self.tools.values())
        

