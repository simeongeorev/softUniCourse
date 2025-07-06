resources_dict = {}
resources_list = []

while True:
    command = input()

    if command == "stop":
        break

    resources_list.append(command)

for i in range(0, len(resources_list), 2):
    if resources_list[i] not in resources_dict.keys():
        resources_dict[resources_list[i]] = 0
    resources_dict[resources_list[i]] += int(resources_list[i + 1])

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
