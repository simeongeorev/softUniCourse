my_stack = []
n = int(input())

for _ in range(n):
    command = input()

    if command.startswith("1"):
        number = int(command.split()[1])
        my_stack.append(number)
    elif my_stack:
        if command.startswith("2"):
            my_stack.pop()
        elif command.startswith("3"):
            print(sorted(my_stack)[-1])
        elif command.startswith("4"):
            print(sorted(my_stack)[0])

print(*reversed(my_stack), sep=", ")