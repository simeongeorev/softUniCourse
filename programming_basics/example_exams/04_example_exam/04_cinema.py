room_capacity = int(input())

total_people_entered = 0
total_money_gathered = 0

while True:

    command = input()

    if command == "Movie time!":
        print(f"There are {room_capacity - total_people_entered} seats left in the cinema.")
        break

    n_people_entering = int(command)

    total_people_entered += n_people_entering

    if total_people_entered > room_capacity:
        print("The cinema is full.")
        break

    money_gathered_for_current_entering = n_people_entering * 5

    if n_people_entering % 3 == 0:
        money_gathered_for_current_entering -= 5

    total_money_gathered += money_gathered_for_current_entering

print(f"Cinema income - {total_money_gathered} lv.")