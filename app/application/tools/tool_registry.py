from app.domain.ports.tool import Tool


class ToolRegistry:

    def __init__(self, tools: list[Tool]):
        self.tools= {
            tool.name: tools
            for tool in tools
        }

    def get(self, name: str)-> Tool:
        return self.tools[name]

    def all(self)-> list[Tool]:
        return list(self.tools.values())
        

