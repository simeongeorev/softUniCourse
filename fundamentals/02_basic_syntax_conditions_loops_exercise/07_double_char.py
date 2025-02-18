while True:

    string_reversed = ""

    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    for i in range(0, len(command)):
        string_reversed += command[i] * 2

    print(string_reversed)