targets_list = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        targets_list = list(map(str, targets_list))
        targets_list_string = "|".join(targets_list)
        print(targets_list_string)
        break

    command_list = command.split()
    command_type = command_list[0]
    command_index = int(command_list[1])

    targets_list_range = range(len(targets_list))

    if command_type == "Shoot":
        power = int(command_list[2])

        if command_index in targets_list_range:
            targets_list[command_index] -= power

            if targets_list[command_index] <= 0:  # target shot
                del targets_list[command_index]

    if command_type == "Add":
        value_to_add = int(command_list[2])

        if command_index in targets_list_range:
            targets_list.insert(command_index, value_to_add)
        else:
            print("Invalid placement!")

    if command_type == "Strike":
        radius_of_indexes = int(command_list[2])

        left_indexes = command_index - radius_of_indexes
        right_indexes = command_index + radius_of_indexes

        if left_indexes in targets_list_range and right_indexes in targets_list_range:
            del targets_list[left_indexes:right_indexes + 1]
        else:
            print("Strike missed!")

