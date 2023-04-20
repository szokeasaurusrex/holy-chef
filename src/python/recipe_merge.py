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
        # pylint: disable=line-too-long
        system_prompt = """The user will provide you the title and ingredients of two recipes.Your job is to invent a never-before-seen recipe inspired by the two given recipes.
        Please output the recipe you invent in JSON format. The JSON should include the following fields: 
        -"title": The recipe title, as a string
        - "ingredients": The ingredients, as an array of strings, with each string containing one ingredient
        - "instructions": The instructions, as an array of strings, 
        with each string containing one step for the recipe """
        print(system_prompt)
        user_input = "Recipe 1. Title: " + recipelist1['title'] + "." + "Ingredients: " + recipelist1['ingredients'] +  "Recipe 2. Title: " + recipelist2['title'] + "." + "Ingredients: " + recipelist2['ingredients'] # pylint: disable=unsubscriptable-object,disable=line-too-long

        result = chat_gpt_manager.text_completion(system_prompt,user_input)
        return result
