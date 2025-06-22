chat_list = []

while True:
    command = input()

    if command == "end":
        break

    command_list = command.split()
    command = command_list[0]
    chat_message = command_list[1]

    if command == "Chat":
        chat_list.append(chat_message)

    elif command == "Delete":
        if chat_message in chat_list:
            chat_list.remove(chat_message)

    elif command == "Edit":
        if chat_message in chat_list:
            edited_message = command_list[2]
            message_index = chat_list.index(chat_message)
            chat_list[message_index] = edited_message

    elif command == "Pin":
        if chat_message in chat_list:
            chat_list.remove(chat_message)
            chat_list.append(chat_message)

    elif command == "Spam":
        spam_message_list = command_list[1:]
        for message in spam_message_list:
            chat_list.append(message)

for chat in chat_list:
    print(chat)

