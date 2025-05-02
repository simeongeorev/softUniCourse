train_wagons_count = int(input())
train_wagons = list(map(int, [0] * train_wagons_count))

while True:
    command = input()
    if command == "End":
        break

    command_list = command.split()

    if "add" in command:
        train_wagons[-1] += int(command_list[1])

    elif "insert" in command:
        index = int(command_list[1])
        people_count = int(command_list[2])
        train_wagons[index] += people_count

    elif "leave" in command:
        index = int(command_list[1])
        people_count = int(command_list[2])
        train_wagons[index] -= people_count

print(train_wagons)