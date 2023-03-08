import re  # pip install regex


with open('allrecipe_source.txt', 'r', encoding='UTF-8') as source_file:
    contents = source_file.read()
    url = re.findall(
        r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]"
        r"{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", contents)
    with open("recipe_url.csv", 'w', newline='', encoding='UTF-8') as csvfile:

        # writer = csv.writer(rec)

        for i, url in enumerate(url):
            # writer.writerow(f"https://www.allrecipes.com{url[1]}")
            csvfile.write(f"https://www.allrecipes.com{url[1]},\n")

