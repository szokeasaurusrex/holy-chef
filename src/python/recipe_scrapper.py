import csv
import json
from recipe_scrapers import scrape_me

def single_json_out():
    """Function that outputs a single json with all recipes in csv file."""
    with open('../recipe_url.csv', 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open("../recipes/master_mar_8_v4.json", 'w', encoding='UTF-8') as json_file:
            for row in csv_reader:
                recipe_url= row[0]
                scraper = scrape_me(recipe_url)
                to_json = scraper.to_json()
                json.dump(to_json, json_file)
                json_file.write("\n")

def multiple_json_out():
    """Function that outputs multiple jsons with all recipes in csv file."""
    with open('../recipe_url.csv', 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            recipe_url= row[0]
            scraper = scrape_me(recipe_url)
            recipe_name = scraper.title()
            recipe_name = recipe_name.replace(' ', '_').lower()
            with open(f"../recipes/{recipe_name}.json", 'w', encoding='UTF-8') as json_file:
                to_json = scraper.to_json()
                json.dump(to_json, json_file)
                json_file.write("\n")

if __name__ == "__main__":
    single_json_out()
