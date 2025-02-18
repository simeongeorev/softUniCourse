n = int(input())

for _ in range(n):
    command = input()

    string_is_pure = True

    for i in range(len(command)):

        if command[i] in ",._":
            string_is_pure = False
            break

    if string_is_pure:
        print(f"{command} is pure.")
    else:
        print(f"{command} is not pure!")