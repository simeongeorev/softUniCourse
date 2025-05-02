notes_list = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    command_list = command.split("-")
    index = int(command_list[0]) - 1
    notes_list.pop(index)
    notes_list.insert(index, command_list[1])

result = [note for note in notes_list if note != 0]
print(result)