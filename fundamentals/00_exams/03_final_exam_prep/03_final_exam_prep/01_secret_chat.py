import re

secret_message = list(input())

while True:
    command = input()

    if command == "Reveal":
        break

    command_list = command.split(":|:")
    command = command_list[0]
    secret_message_str = "".join(secret_message)

    if command == "InsertSpace":
        index = int(command_list[1])
        secret_message.insert(index, " ")
        print("".join(secret_message))

    elif command == "Reverse":
        substring = command_list[1]

        if substring in secret_message_str:
            matches = re.finditer(re.escape(rf"{substring}"), secret_message_str)
            for match in matches:
                start_index = match.start()
                end_index = match.end()
                break
            to_extract = secret_message[start_index:end_index]
            del secret_message[start_index:end_index]
            secret_message += to_extract[::-1]
            print("".join(secret_message))
        else:
            print("error")

    elif command == "ChangeAll":
        substring = command_list[1]
        replacement = command_list[2]
        secret_message = list(re.sub(re.escape(rf"{substring}"), replacement, secret_message_str))
        print("".join(secret_message))

secret_message_str = "".join(secret_message)
print(f"You have a new text  message: {secret_message_str}")