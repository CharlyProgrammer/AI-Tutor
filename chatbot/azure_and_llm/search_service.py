
from dotenv import load_dotenv
import os
import requests
load_dotenv(dotenv_path=os.path.dirname(os.getcwd())+'/Proyecto_de_fase_3/app/llms_and_rag/.env')
#print(load_dotenv(dotenv_path=os.path.dirname(os.getcwd())+'/Proyecto_de_fase_3/app/llms_and_rag/.env'))
class search_info:
    def __init__(self,key_service,endpoint_service,index_name):
        self.key_service=key_service
        self.endpoint_service=endpoint_service
        self.index_name=index_name
        self.key=""
        self.endpoint=""
        self.index=""
        self.headers={}
        self.search_url=""
    def init_service(self):
        self.key=os.getenv(self.key_service)
        self.endpoint=os.getenv(self.endpoint_service)
        self.index=os.getenv(self.index_name)
        
        self.headers = {
        "Content-Type": "application/json",
        "api-key": self.key,
        }
        self.search_url = f"{self.endpoint}/indexes/{self.index}/docs/search?api-version=2021-04-30-Preview"
        return self.headers,self.search_url 
       
    def retrieve_documents(self,query,headers,search_url):
        """Obtiene documentos relevantes desde Azure Cognitive Search."""
    
        payload = {
            "search": query,
            "top": 1, 
        }
    
        response = requests.post(search_url, json=payload, headers=headers)
        response.raise_for_status()
        results = response.json()
    
        return [doc["content"] for doc in results["value"]]