import json

from elastic_manager import ElasticManager

def main():
    """main"""
    recipe_list = []
    with open('python/master_mar_8_v4.json', encoding = 'UTF-8') as recipes:
        for json_obj in recipes:
            recipe_dict = json.loads(json_obj)
            recipe_list.append(recipe_dict)
    manager = ElasticManager("http://localhost:9200")
    manager.bulk_insert_document("recipes_v2", recipe_list)

if __name__ == "__main__":
    main()
