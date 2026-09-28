from app.domain.ports.tool import Tool

def to_openai_tool(tool : Tool)-> dict:
    return {
        "type": "function",
        "name": tool.name,
        "description": tool.description,
        "parameters": tool.parameters
    }