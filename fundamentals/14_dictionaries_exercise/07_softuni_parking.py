n_commands = int(input())
parking_dict = {}

for i in range(n_commands):

    command_list = input().split()

    command = command_list[0]
    username = command_list[1]

    if command == "register":
        lic_plate_num = command_list[2]
        if username in parking_dict.keys():
            print(f"ERROR: already registered with plate number {parking_dict[username]}")
        else:
            parking_dict[username] = lic_plate_num
            print(f"{username} registered {lic_plate_num} successfully")
    elif command == "unregister":
        if username not in parking_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking_dict[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking_dict.items():
    print(f"{username} => {license_plate_number}")

