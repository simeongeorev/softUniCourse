list_of_gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command_as_list = command.split()
    instruction = command_as_list[0]

    if instruction == "OutOfStock":
        gift_to_remove = command_as_list[1]
        changed_list = [gift if gift != gift_to_remove else "None" for gift in list_of_gifts]
        list_of_gifts = changed_list

    elif instruction == "Required":
        new_gift = command_as_list[1]
        index = int(command_as_list[2])
        if index in range(len(list_of_gifts)):
            list_of_gifts[index] = new_gift
        else:
            continue

    elif instruction == "JustInCase":
        new_gift = command_as_list[1]
        list_of_gifts[-1] = new_gift

list_to_print = [gift for gift in list_of_gifts if gift != "None"]

print(" ".join(list_to_print))