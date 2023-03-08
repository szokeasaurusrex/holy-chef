import os 
import json

dir_name = "recipes"


recipe_list = []

for i, recipe_path in enumerate(os.listdir(dir_name)):
    with open(f"../recipes/{recipe_path}", 'w+') as recipe:
        recipe_list.append(json.loads(recipe))
        