shopping_list = input().split("!")

while True:

    command = input()

    if command == "Go Shopping!":
        break

    command_list = command.split()

    command = command_list[0]
    item = command_list[1]

    # add item at the start
    if command.startswith("Urgent"):
        if item in shopping_list:
            continue
        else:
            shopping_list.insert(0, item)

    # delete item if it exists
    if command.startswith("Unnecessary"):
        if item not in shopping_list:
            continue
        else:
            shopping_list.remove(item)

    # edit item
    if command.startswith("Correct"):
        if item not in shopping_list:
            continue
        else:
            correct_item = command_list[2]
            item_index = shopping_list.index(item)
            shopping_list[item_index] = correct_item

    # remove item and add it at the end of the list
    if command.startswith("Rearrange"):
        if item not in shopping_list:
            continue
        else:
            shopping_list.remove(item)
            shopping_list.append(item)

shopping_list_str = ", ".join(shopping_list)
print(shopping_list_str)