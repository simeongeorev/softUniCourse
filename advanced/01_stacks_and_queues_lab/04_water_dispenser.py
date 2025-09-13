from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{water_quantity} liters left")
        break
    elif command.startswith("refill"):
        litres_to_refill = command.split()[1]
        water_quantity += int(litres_to_refill)
    else:
        litres = int(command)
        if litres <= water_quantity:
            water_quantity -= litres
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")