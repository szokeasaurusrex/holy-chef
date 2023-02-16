from elasticsearch import Elasticsearch
"""from elasticsearch.client import IndicesClient"""

class Elastic_Manager:
    def __init__(self, port):
        self.es_client = Elasticsearch(port)
    def retrieve_recipe(self, recipe_infopush):
        print("Hello")
    def insert_document(self, index_name, document_JSON):
        self.es_client.index(index=index_name, document=document_JSON)
