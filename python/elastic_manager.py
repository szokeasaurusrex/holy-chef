from elasticsearch import Elasticsearch

class ElasticManager:
    """ElasticManager"""
    def __init__(self, port):
        self.es_client = Elasticsearch(port)
    def retrieve_recipe(self, recipe_infopush):
        """retrieve_recipe"""
        print(recipe_infopush)
    def insert_document(self, index_name, document_json):
        """insert_document"""
        self.es_client.index(index=index_name, document=document_json)
