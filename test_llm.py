from app.infrastructure.llm.client import get_llm_client
from app.core.config import settings

client= get_llm_client()  #calls the function we already created 

#this is where actual api call happens   
response = client.responses.create(
    model= settings.llm_model,
    input= "Explain FastAPI in one sentence."
)   #here we are saying send a request to the OpenAI API and generate a response


#the response isn't just string it contains id, model, status, output, output_text 
print(response.output_text) #output_text is the convenient way to get the generated_text