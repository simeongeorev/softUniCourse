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
        first_part_list = list(numbers_list[:index_to_split])
        del numbers_list[:index_to_split]
        numbers_list += first_part_list

    if "max" in command:
        largest_n = -math.inf
        index_of_num = 0
        if command_list[1] == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 == 0:
                    if numbers_list[i] >= largest_n:
                        largest_n = numbers_list[i]
                        index_of_num = i
            print(index_of_num)
        elif command_list[1] == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 != 0:
                    if numbers_list[i] >= largest_n:
                        largest_n = numbers_list[i]
                        index_of_num = i
            print(index_of_num)
        if largest_n == -math.inf:
            print("No matches")

    if "min" in command:
        smallest_n = math.inf
        index_of_num = 0
        if command_list[1] == "even":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 == 0:
                    if numbers_list[i] <= smallest_n:
                        smallest_n = numbers_list[i]
                        index_of_num = i
            print(index_of_num)
        elif command_list[1] == "odd":
            for i in range(len(numbers_list)):
                if numbers_list[i] % 2 != 0:
                    if numbers_list[i] >= smallest_n:
                        smallest_n = numbers_list[i]
                        index_of_num = i
            print(index_of_num)
        if smallest_n == -math.inf:
            print("No matches")

    if "first" in command:
        ...
    if "last" in command:
        ...


print(numbers_list)