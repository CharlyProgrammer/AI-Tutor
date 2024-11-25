from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.dirname(os.getcwd())+'/chatbot/chatbot/azure_and_llm/.env')

class model_completion:
    def __init__(self,key_model,model_version):
        self.key_model=key_model
        self.model_version=model_version
        self.llama_key=""
        self.llama_client=""
        self.llama_model=""
    
    def init_model(self):
        
        
        
        self.llama_key = os.getenv(self.key_model)
        self.llama_client = Groq(api_key=self.llama_key)
        return self.llama_client
        
    
    def generate_response(self,client,prompt,temperature):
        self.llama_model = os.getenv(self.model_version)
       
        messages=[
            {
                "role": "system",
                "content": "Tu eres un asistente a quien le gusta responder diferentes preguntas de forma concisa y precisa."
            },
            {
                "role": "user",
                "content": prompt,
            }
        ]
        response = client.chat.completions.create(
                        model=self.llama_model,
                        temperature=temperature,
                        messages=messages,
                        max_tokens=4096
                    )
        return response.choices[0].message.content