energy = int(input())

won_battles_count = 0

while True:
    command = input()

    if command == "End of battle":
        print(f"Won battles: {won_battles_count}. Energy left: {energy}")
        break

    battle_points = int(command)

    if energy >= battle_points:
        energy -= battle_points
        won_battles_count += 1
        if won_battles_count % 3 == 0:
            energy += won_battles_count

    elif energy < battle_points:
        print(f"Not enough energy! Game ends with {won_battles_count} won battles and {energy} energy")
        break


