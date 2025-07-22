import re

text = input()

all_links = []

while text:
    pattern = r"[w]{3}[.][a-zA-Z0-9-\.]+(?:[.][a-z]+)"

    all_links += re.findall(pattern, text)

    text = input()

for link in all_links:
    print(link)