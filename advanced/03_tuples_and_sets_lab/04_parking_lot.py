number_of_commands = int(input())
in_set = set()
for _ in range(number_of_commands):
    command, plate = input().split(", ")
    if command == "IN":
        in_set.add(plate)
    elif command == "OUT":
        in_set.remove(plate)

print("\n".join(in_set) if in_set else "Parking Lot is Empty")