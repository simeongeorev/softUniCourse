friends_list = input().split(", ")

blacklisted_names_count = 0
lost_names_count = 0

while True:
    command = input()

    if command == "Report":
        break

    command_list = command.split()
    command = command_list[0]

    if command == "Blacklist":
        name_to_blacklist = command_list[1]

        if name_to_blacklist in friends_list:
            name_index = friends_list.index(name_to_blacklist)
            friends_list[name_index] = "Blacklisted"

            print(f"{name_to_blacklist} was blacklisted.")
            blacklisted_names_count += 1
        else:
            print(f"{name_to_blacklist} was not found.")

    elif command == "Error":
        index = int(command_list[1])

        if (index in range(0, len(friends_list)) and
            friends_list[index] != "Blacklisted" and friends_list[index] != "Lost"):

            name_to_lose = friends_list[index]
            friends_list[index] = "Lost"
            print(f"{name_to_lose} was lost due to an error.")
            lost_names_count += 1

    elif command == "Change":
        index = int(command_list[1])
        new_name = command_list[2]

        if index in range(0, len(friends_list)):
            name_to_change = friends_list[index]
            friends_list[index] = new_name
            print(f"{name_to_change} changed his username to {new_name}.")

print(f"Blacklisted names: {blacklisted_names_count}")
print(f"Lost names: {lost_names_count}")
print(" ".join(friends_list))