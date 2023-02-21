import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

class ElasticManager:
    """ElasticManager"""
    def __init__(self, port):
        load_dotenv()
        self.es_client = Elasticsearch(
            port,
            verify_certs=False,
            basic_auth=('elastic', os.environ['elastic_password'])
        )

    def retrieve_recipe(self, ingredient_string, time_cook):
        """retrieve_recipe"""
        query_body = {
            "bool":
            {
                "must": [
                    {
                        "range": {
                            "total_time": {
                                "lte" : time_cook
                            }
                        }
                    }
                ],
                "should": [
                    {
                        "match": {
                                "ingredients": ingredient_string
                            }
                        }
                ]
            }
        }
        results = self.es_client.search(index="recipes", query=query_body)
        return [result['_source'] for result in results['hits']['hits']]

    def insert_document(self, index_name, document_json):
        """insert_document"""
        self.es_client.index(index=index_name, document=document_json)
