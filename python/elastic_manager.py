from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

class ElasticManager:
    """ElasticManager"""
    def __init__(self, port):
        load_dotenv()
        self.es_client = Elasticsearch(port, verify_certs=False, basic_auth=('elastic', os.environ['elastic_password']))

    def retrieve_recipe(self, ingredient_array, time_cook):
        """retrieve_recipe"""

        ingredient_string = self.ingredients_to_string(ingredient_array)
        

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
        result = self.es_client.search(index="recipes", query=query_body)
        print("Result ", result["hits"]["hits"])
        return result

    def ingredients_to_string(self, ingredient_array):
        """ingredientsToString"""
        ingredient_string = ' '

        for ingredient in ingredient_array:
            if ingredient_string == ' ':
                ingredient_string += ingredient
            else:
                ingredient_string += "," + ingredient

        return ingredient_string


    def insert_document(self, index_name, document_json):
        """insert_document"""
        self.es_client.index(index=index_name, document=document_json)
