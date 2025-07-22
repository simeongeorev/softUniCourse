import re

text = input()


pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[a-zA-Z0-9_.-]*[a-zA-Z0-9]+[@][a-zA-Z0-9]+[a-zA-Z0-9-.]*[a-zA-Z0-9]+[\.][a-zA-Z0-9]+\b"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())