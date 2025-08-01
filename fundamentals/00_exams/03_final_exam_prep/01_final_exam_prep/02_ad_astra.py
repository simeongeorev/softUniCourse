import re

text = input()

pattern = r"(?P<sym>[#|])([a-zA-Z ]+)(?P=sym)([0-9]{2}[\/][0-9]{2}[\/][0-9]{2})(?P=sym)([0-9]|[1-9][0-9]{0,4})(?P=sym)"

matches = re.findall(pattern, text)
total_cals = 0

for match in matches:
    total_cals += int(match[3])

days_to_last = total_cals // 2000

print(f"You have food to last you for: {days_to_last} days!")

for match in matches:
    food = match[1]
    date = match[2]
    nutrition = match[3]
    print(f"Item: {food}, Best before: {date}, Nutrition: {nutrition}")

