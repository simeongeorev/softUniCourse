text = input()

while (command := input()) != "Done":
    command_list = command.split(" ")
    command = command_list[0]

    if command == "TakeOdd":
        text = "".join([text[i] for i in range(1, len(text), 2)])
        print(text)

    elif command == "Cut":
        index, length = int(command_list[1]), int(command_list[2])
        cut = text[index:index + length]
        text = text.replace(cut, "", 1)
        print(text)

    elif command == "Substitute":
        substring, substitute = command_list[1], command_list[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")

print(f"Your password is: {text}")
