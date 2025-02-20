while True:

    command = input()

    if command == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if command == "Voldemort":
        print("You must not speak of that name!")
        break

    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")

    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")

    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")

    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")




