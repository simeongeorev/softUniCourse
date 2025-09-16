first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))
n = int(input())
for i in range(n):
    command = input().split()

    first_command = command[0]
    second_command = command[1]

    if first_command == "Add":
        if second_command == "First":
            for number in command[2:]:
                first_set.add(int(number))

        elif second_command == "Second":
            for number in command[2:]:
                second_set.add(int(number))

    elif first_command == "Remove":
        if second_command == "First":
            for number in command[2:]:
                if int(number) in first_set:
                    first_set.remove(int(number))

        elif second_command == "Second":
            for number in command[2:]:
                if int(number) in second_set:
                    second_set.remove(int(number))

    elif first_command == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(', '.join(str(el) for el in sorted(list(first_set))))
print(', '.join(str(el) for el in sorted(list(second_set))))
