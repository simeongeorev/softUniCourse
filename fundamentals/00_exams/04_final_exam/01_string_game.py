text = input()

while (command := input()) != "Done":
    if command.startswith("End"):
        end_substring = command[4:]

        substring_len = len(end_substring)
        text_ending = text[-substring_len:]
        if text_ending == end_substring:
            print(True)
        else:
            print(False)
        continue

    command_list = command.split()
    command = command_list[0]

    if command == "Change":
        char = command_list[1]
        replacement = command_list[2]

        text = text.replace(char, replacement)
        print(text)

    elif command == "Includes":
        substring = command_list[1]

        if substring in text:
            print(True)
        else:
            print(False)



    elif command == "Uppercase":
        text = text.upper()
        print(text)

    elif command == "FindIndex":
        char = command_list[1]
        print(text.index(char))

    elif command == "Cut":
        start_index = int(command_list[1])
        count = int(command_list[2])

        text = text[start_index:start_index + count]
        print(text)
