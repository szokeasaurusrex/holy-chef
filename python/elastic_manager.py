from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

class Elastic_Manager:
    
    def __init__(self, port):
        self.es_client = Elasticsearch("http://localhost:9200")
    
    def retrieveRecipe(self, recipeInfo):
        
    
        
        
        
    
    