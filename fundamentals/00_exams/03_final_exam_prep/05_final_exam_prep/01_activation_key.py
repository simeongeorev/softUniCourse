raw_key = input()

while (command := input()) != "Generate":
    command_list = command.split(">>>")
    command = command_list[0]

    if command == "Contains":
        substring = command_list[1]

        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        next_command = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])

        sliced = raw_key[start_index:end_index]

        if next_command == "Upper":
            sliced = sliced.upper()
        elif next_command == "Lower":
            sliced = sliced.lower()

        raw_key = raw_key[:start_index] + sliced + raw_key[end_index:]
        print(raw_key)

    elif command == "Slice":
        start_index = int(command_list[1])
        end_index = int(command_list[2])

        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

print(f"Your activation key is: {raw_key}")
