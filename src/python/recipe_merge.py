
import json
from chatgpt_manager import ChatGPTManager


class MergeRecipes:
    """merge_recipes"""

    def join_strings(self,data,delim, json_field):
        "join_string"
        field = data[json_field]
        field = delim.join(field)
        data[json_field] = field

    #Required Fields for recipelist1 and recipelist2
    # - "title"
    # - "ingredients"
    def generate_merged_recipe(self, recipelist1, recipelist2):
        """generate_merged_recipe"""
        chat_gpt_manager = ChatGPTManager()
        system_prompt = """The user will provide you the title and ingredients of two recipes.Your job is to invent a never-before-seen recipe inspired by the two given recipes.
        Please output the recipe you invent in JSON format. The JSON should include the following fields: 
        -"title": The recipe title, as a string
        - "ingredients": The ingredients, as an array of strings, with each string containing one ingredient
        - "instructions": The instructions, as an array of strings, 
        with each string containing one step for the recipe """
        print(system_prompt)
        user_input = "Recipe 1. Title: " + recipelist1['title'] + "." + "Ingredients: " + recipelist1['ingredients'] +  "Recipe 2. Title: " + recipelist2['title'] + "." + "Ingredients: " + recipelist2['ingredients'] # pylint: disable=unsubscriptable-object

        result = chat_gpt_manager.text_completion(system_prompt,user_input)
        return result

#Delete Once Connected to Front End
def main():
    """main"""
    generator = MergeRecipes()
    recipe_list1 = {
        "title": "Kung Pao Orange Chicken",
        "ingredients": """1 pound boneless, skinless chicken breast, cut into bite-sized pieces, 
                        1/2 cup cornstarch,1/4 cup vegetable oil,
                        1/2 cup diced green bell pepper, 1/2 cup diced red bell pepper"""
    }

    recipe_list2 = {
        "title" : "Beef Wellington",
        "ingredients": """2 lb beef tenderloin, 1 lb puff pastry, 1 egg yolk, beaten,
                         Salt and black pepper, 1/4 cup dijon mustard, 8-10 thin slices of prosciutto, 2 cups chopped mushrooms, 
                         1/2 onion, finely chopped, 2 cloves garlic, minced, 2 tbsp butter, 
                         1/4 cup dry white wine,1 tbsp chopped fresh thyme, 2 tbsp olive oil"""
    }
    result = generator.generate_merged_recipe(recipe_list1,recipe_list2)
    print(result)
    recipe_json = json.loads(result)

    #Joins the instruction list into a single string
    generator.join_strings(recipe_json," ", 'instructions')

    print(recipe_json)

if __name__ == "__main__":
    main()
