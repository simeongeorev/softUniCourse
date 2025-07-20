force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if " | " in command:
        force_side, force_user = command.split(" | ")

        # creates a new side if not existing
        if force_side not in force_book.keys():
            force_book[force_side] = []

        # checks if the user is existing in any of the sides
        force_user_exists = False
        for force_users in force_book.values():
            if force_user in force_users:
                force_user_exists = True

        # if user is not existing - add them
        if not force_user_exists:
            force_book[force_side] += [force_user]

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")

        # checks if the user is existing in any of the sides and removes him
        for force_users in force_book.values():
            if force_user in force_users:
                force_users.remove(force_user)

        # creates a new side if not existing
        if force_side not in force_book.keys():
            force_book[force_side] = []

        # add the new user to the corresponding side
        force_book[force_side] += [force_user]

        print(f"{force_user} joins the {force_side} side!")

for force_side, force_users in force_book.items():
    if not force_users:
        del force_side
        continue
    print(f"Side: {force_side}, Members: {len(force_users)}")
    for name in force_users:
        print(f"! {name}")






