phones = {}

while True:
    command = input()

    if "-" not in command:
        break

    name, number = command.split("-")
    phones[name] = number

for _ in range(int(command)):
    name_check = input()
    if name_check in phones.keys():
        print(f"{name_check} -> {phones[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")