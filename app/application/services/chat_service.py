from app.domain.ports.llm import LLM

#Application layer service 
class ChatService:
    def __init__(self, llm):
      self.llm = llm

    def chat(self, message:str)->str:
        return self.llm.generate(message)    
