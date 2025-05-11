input_list = input().split()
# no_whitespace_input_line = list(filter(lambda char: char != " ", input_line))

while True:
    command = input().split()
    if "merge" in command:
        new_list = []
        startIndex, endIndex = int(command[1]), int(command[2])
        if startIndex > len(input_list) - 1:
            startIndex = len(input_list) - 1
        if endIndex > len(input_list) - 1:
            endIndex = len(input_list)
        merged_string = "".join(input_list[startIndex:endIndex])
        for i in range(len(input_list)):
            if input_list[i] in merged_string:
                # new_list.append(merged_string)
                input_list[i] = merged_string
            # else:
            #     new_list.append(input_list[i])
        print("before set - ", input_list)
        input_list = list(set(input_list))

        print("the merged word - ", merged_string)
        print("after the set - ", input_list)


    elif "divide" in command:
        break
    elif command == "3:1":
        break
