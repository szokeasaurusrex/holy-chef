import re  # pip install regex


f = open('allrecipe_source.txt', 'r', encoding='UTF-8')
contents = f.read()
url = re.findall(
    r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]"
    r"{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", contents)
with open("recipe_url.csv", 'w', newline='', encoding='UTF-8') as csvfile:

    # writer = csv.writer(rec)

    for i, url in enumerate(url):
        # writer.writerow(f"https://www.allrecipes.com{url[1]}")
        csvfile.write(f"https://www.allrecipes.com{url[1]},\n")

f.close()
