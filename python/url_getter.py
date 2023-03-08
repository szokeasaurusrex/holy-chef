import re # pip install regex
import csv # pip install csv



f = open('allrecipe_source.txt', 'r')
contents = f.read()
url = re.findall(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)",contents)
with open("recipe_url.csv", 'w', newline ='') as csvfile:

    # writer = csv.writer(rec)

    for i, url in enumerate(url):
        # writer.writerow(f"https://www.allrecipes.com{url[1]}")
        csvfile.write(f"https://www.allrecipes.com{url[1]},\n")

        
f.close()
