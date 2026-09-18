from openai import OpenAI


#Application layer service 
class ChatService:
    def __init__(self, client: OpenAI, model:str):
       self.client = client 
       self.model= model

    def chat(self, message:str)->str:
        response = self.client.responses.create(
            model= self.model,
            input=message,
        )
        return response.output_text
    
