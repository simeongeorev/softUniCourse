player_name = input()
points_left = 301
successful_hits = 0
unsuccessful_hits = 0
command = input()
while command != "Retire":
    field = command
    points_hit = int(input())

    if field == "Double":
        points_hit *= 2
    elif field == "Triple":
        points_hit *= 3

    if points_left >= points_hit:
        points_left -= points_hit
        successful_hits += 1
    else:
        unsuccessful_hits += 1

    if points_left == 0:
        print(f"{player_name} won the leg with {successful_hits} shots.")
        break
    command = input()
else:
    print(f"{player_name} retired after {unsuccessful_hits} unsuccessful shots.")