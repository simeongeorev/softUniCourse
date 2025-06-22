int_array = list(map(int, input().split()))

while True:
    command = input()

    if command == 'end':
        break

    elif command == 'decrease':
        int_array = list(map(lambda x: x - 1, int_array))

    else:
        command_list = command.split()

        command = command_list[0]
        index_1 = int(command_list[1])
        index_2 = int(command_list[2])

        if command == 'swap':
            int_array[index_1], int_array[index_2] = int_array[index_2], int_array[index_1]

        if command == 'multiply':
            int_array[index_1] = int_array[index_1] * int_array[index_2]

list_as_string = ', '.join(list(map(str, int_array)))
print(list_as_string)