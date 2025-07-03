my_dict = {}

while (command := input()) != "statistics":

    command_list = command.split(":")

    key = command_list[0]
    value = int(command_list[1])

    if key not in my_dict.keys():
        my_dict[key] = value
    else:
        my_dict[key] += value

print("Products in stock:")
for key, value in my_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")

