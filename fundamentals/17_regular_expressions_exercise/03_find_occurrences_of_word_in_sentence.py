import re

text = input()
search_word = input()

pattern = rf"\b{search_word}\b"

matches = re.findall(pattern, text, flags=re.I)

print(len(matches))

