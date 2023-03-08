import os
import json

DIR_NAME = "recipes"


recipe_list = []

for i, recipe_path in enumerate(os.listdir(DIR_NAME)):
    with open(f"../recipes/{recipe_path}", 'w+', encoding='UTF-8') as recipe:
        recipe_list.append(json.loads(recipe))
        