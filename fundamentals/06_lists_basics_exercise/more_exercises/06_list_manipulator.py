import math

numbers_list = input().split()

# turn the list into integers
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

while True:

    command = input()

    if command == "end":
        break

    command_list = command.split()

    if "exchange" in command:
        index_to_split = int(command_list[1])
        if index_to_split < 0 or index_to_split >= len(numbers_list):
            print("Invalid index")
            continue
        first_part_list = list(numbers_list[:index_to_split+1])
        del numbers_list[:index_to_split+1]
        numbers_list += first_part_list

    if "max" in command:
        largest_n = -math.inf
        index_of_num = -1
        if command_list[1] == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 == 0:
                    if numbers_list[i] >= largest_n:
                        largest_n = numbers_list[i]
                        index_of_num = i
            if index_of_num == -1:
                print("No matches")
            else:
                print(index_of_num)

        elif command_list[1] == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 != 0:
                    if numbers_list[i] >= largest_n:
                        largest_n = numbers_list[i]
                        index_of_num = i
            if index_of_num == -1:
                print("No matches")
            else:
                print(index_of_num)

    if "min" in command:
        smallest_n = math.inf
        index_of_num = -1
        if command_list[1] == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 == 0:
                    if numbers_list[i] <= smallest_n:
                        smallest_n = numbers_list[i]
                        index_of_num = i
            if index_of_num == -1:
                print("No matches")
            else:
                print(index_of_num)

        elif command_list[1] == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 != 0:
                    if numbers_list[i] <= smallest_n:
                        smallest_n = numbers_list[i]
                        index_of_num = i
            if index_of_num == -1:
                print("No matches")
            else:
                print(index_of_num)

    if "first" in command:
        count_input = int(command_list[1])
        first_list = []
        counter = 0
        if count_input > len(numbers_list):
            print("Invalid count")
            continue

        if command_list[2] == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 == 0:
                    first_list.append(numbers_list[i])
                    counter += 1
                if counter == count_input:
                    print(first_list)
                    break
            else:
                print(first_list)

        elif command_list[2] == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 != 0:
                    first_list.append(numbers_list[i])
                    counter += 1
                if counter == count_input:
                    print(first_list)
                    break
            else:
                print(first_list)

    if "last" in command:
        count_input = int(command_list[1])
        last_list = []
        counter = 0
        if count_input > len(numbers_list):
            print("Invalid count")
            continue

        if command_list[2] == "even":
            for i in range(len(numbers_list) - 1, -1, -1):
                if numbers_list[i] % 2 == 0:
                    last_list.append(numbers_list[i])
                    counter += 1
                if counter == count_input:
                    print(last_list)
                    break
            else:
                print(last_list)

        elif command_list[2] == "odd":
            for i in range(len(numbers_list) - 1, -1, -1):
                if numbers_list[i] % 2 != 0:
                    last_list.append(numbers_list[i])
                    counter += 1
                if counter == count_input:
                    print(last_list)
                    break
            else:
                    print(last_list)

print(numbers_list)

# TODO Not getting the full score. Should be rewritten with functions.