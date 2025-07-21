import re

text = input()

regex = r"(\d{2})(?P<sep>[/.-])([A-Z][a-z]{2})(?P=sep)(\d{4})\b"

matches = re.findall(regex, text)

for group in matches:
    day = group[0]
    month = group[2]
    year = group[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")