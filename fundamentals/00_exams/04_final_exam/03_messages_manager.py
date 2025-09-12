messages_limit = int(input())
messages_dict = {}

while (command := input()) != "Statistics":
    command_list = command.split("=")
    command = command_list[0]

    if command == "Add":
        username = command_list[1]
        sent = int(command_list[2])
        received = int(command_list[3])

        if username not in messages_dict:
            messages_dict[username] = sent + received

    elif command == "Message":
        sender = command_list[1]
        receiver = command_list[2]

        if sender in messages_dict.keys() and receiver in messages_dict.keys():
            messages_dict[sender] += 1
            messages_dict[receiver] += 1

            if messages_dict[sender] >= messages_limit:
                print(f"{sender} reached the capacity!")
                del messages_dict[sender]

            if messages_dict[receiver] >= messages_limit:
                print(f"{receiver} reached the capacity!")
                del messages_dict[receiver]

    elif command == "Empty":
        username = command_list[1]

        if username == "All":
            messages_dict.clear()

        if username in messages_dict.keys():
            del messages_dict[username]

n_users = len(messages_dict.keys())
print(f"Users count: {n_users}")
for user in messages_dict.items():
    print(f"{user[0]} - {user[1]}")





















