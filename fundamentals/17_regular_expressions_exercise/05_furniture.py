import re

furniture_names = []
total_price = 0

while True:

    command = input()

    if command == "Purchase":
        break

    pattern = r"^[>]{2}([\w\-.]+)[<]{2}([\d]+(?:[.][\d]+)?)[!]([0-9]+)$"

    matches = re.findall(pattern, command)

    if matches:
        f_name = matches[0][0]
        furniture_names.append(f_name)
        price = float(matches[0][1])
        quantity = int(matches[0][2])
        total_price += price * quantity

print("Bought furniture:")
for furn in furniture_names:
    print(furn)
print(f"Total money spend: {total_price:.2f}")
