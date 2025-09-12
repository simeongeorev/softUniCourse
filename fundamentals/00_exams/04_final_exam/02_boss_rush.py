import re

n = int(input())

for _ in range(n):
    text = input()

    pattern = r"[|]([A-Z]{4,})[|][:][#]([A-Za-z]+[ ][A-Za-z]+)[#]"

    matches = re.findall(pattern, text)

    if matches:
        name = matches[0][0]
        title = matches[0][1]
        print(f"{name}, The {title}\n>> Strength: {len(name)}\n>> Armor: {len(title)}")
    else:
        print("Access denied!")
