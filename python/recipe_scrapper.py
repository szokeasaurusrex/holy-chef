from recipe_scrapers import scrape_me # pip install recipe-scrapers
import csv
import json

single = "\'"
double = "\""
with open('../recipe_url.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open(f"../recipes/master_mar_8_v3.json", 'w') as f:
        for i, row in enumerate(csv_reader):
            # print(f"{i}: {row}")
            recipe_url= row[0]
            scraper = scrape_me(recipe_url)
            # recipe_name = scraper.title()
            # recipe_name = recipe_name.replace(' ', '_').lower()
            # open here for mutiple files
            to_json = scraper.to_json()
            # js = str(to_json).replace(single, double)
            json.dump(to_json, f)