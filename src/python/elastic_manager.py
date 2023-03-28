import os
import csv
from io import StringIO
from elasticsearch import Elasticsearch
from elasticsearch import helpers
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
    
    def _split_str_by_comma(self, comma_separated_string):
        string_as_file = StringIO(comma_separated_string)
        for line in csv.reader(string_as_file):
            for element in line:
                yield element
    
    def _comma_split_query(self, query_field, comma_separated_string):
        return [{
            'match_phrase': {
                query_field: element
            }
        } for element in self._split_str_by_comma(comma_separated_string)]

    def retrieve_recipe(self, recipe_options):
        """retrieve_recipe"""
        dietary_restrictions = recipe_options['dietary_restrictions']

        if 'lactose_intolerant' in recipe_options:
            dietary_restrictions += ',milk, cheese, butter, yogurt,'

        if 'nut_allergy' in recipe_options:
            dietary_restrictions += ',nut,peanut,hazelnut,'

        if 'gluten_free' in recipe_options:
            dietary_restrictions += ',bread,beer,wheat,pasta,'

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
                "must_not": self._comma_split_query('ingredients', dietary_restrictions),
                "should": [
                    *self._comma_split_query('ingredients', recipe_options['ingredients']),
                    *self._comma_split_query('title', recipe_options['liked_foods'])
                ]
            }
        }
        print(query_body)
        results = self.es_client.search(index="recipes_v2", query=query_body)
        return [result['_source'] for result in results['hits']['hits']]

    def bulk_insert_document(self, index_name, input_list):
        """bulk_insert_document"""     
        actions = []
        list_index = 0
        while list_index < len(input_list):

            current_dict = input_list[list_index]

            action = {
                "_index": "recipes_v2",
                "_id": list_index,
                "_source": {
                    "title": current_dict["title"],
                    "total_time": current_dict["total_time"],
                    "ingredients": current_dict["ingredients"],
                    "instructions":current_dict["instructions"],
                    "description": current_dict["description"],
                    "image": current_dict["image"],
                    "ratings":current_dict["ratings"]
                }
            }
            actions.append(action)
            list_index += 1

        helpers.bulk(self.es_client, actions, index = index_name)
