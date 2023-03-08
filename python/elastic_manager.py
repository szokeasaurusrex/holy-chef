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

    def retrieve_recipe(self, recipe_options):
        """retrieve_recipe"""
        dietary_restrictions = recipe_options['dietary_restrictions']

        if 'lactose_intolerant' in recipe_options:
            dietary_restrictions += ' milk cheese butter yogurt '

        if 'nut_allergy' in recipe_options:
            dietary_restrictions += ' nut peanut hazelnut '

        if 'gluten_free' in recipe_options:
            dietary_restrictions += ' bread beer wheat pasta '

        query_body = {
            "bool":
            {
                "must": [
                    {
                        "range": {
                            "total_time": {
                                "lte" : recipe_options['time_to_cook']
                            }
                        }
                    }
                ],
                "must_not": [
                    {
                        "match": {
                            "ingredients": dietary_restrictions
                        }
                    }
                ],
                "should": [
                    {
                        "match": {
                            "ingredients": recipe_options['ingredients']                            
                        }
                    },
                    {
                        "match": {
                            "title": recipe_options['liked_foods']
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
