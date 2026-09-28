from app.domain.ports.llm import LLM
from app.application.tools.tool_definition import to_openai_tool
from app.application.tools.tool_registry import ToolRegistry

class CodeAgent:

    def __init__(
                  self,
                  llm: LLM,
                  tool_registry: ToolRegistry
                    ):
        self.llm = llm
        self.tool_registry = tool_registry

    def run(self, task: str)-> str:
     
        registered_tools = self.tool_registry.all()
    
        print("\n===== TOOL DEBUG =====")
        print("Registry:", self.tool_registry)
        print("Registered tools:", registered_tools)
        print("Registered tools type:", type(registered_tools))
    
        for index, tool in enumerate(registered_tools):
            print(f"Tool {index}:", tool)
            print(f"Tool {index} type:", type(tool))
    
        print("======================\n")
    
        tools = [
            to_openai_tool(tool)
            for tool in registered_tools
        ]

        response=  self.llm.generate_with_tools(
           message= task, 
           tools= tools
       )

        print("\n===========AGENT RESPONSE=============")
        print("Content: ", response.content)
        print("Tool Calls: ", response.tool_calls)
        print("========================================\n")    
        if not response.tool_calls:
           return response.content or ""

       

        for tool_call in response.tool_calls:
             print("\n===========Executing Tool=============")
             print("Tool name: ", tool_call.name)
             print("Arguments: ", tool_call.arguments)
             print("========================================\n") 
           

             tool = self.tool_registry.get(
                tool_call.name
            )

             result = tool.execute(
                **tool_call.arguments
            )
             print("\n===========Tool Result=============")
             print(result)
             print("========================================\n") 
             

             return result

        return ""
           

 
       # return self.llm.generate(prompt)