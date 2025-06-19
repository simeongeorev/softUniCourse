hearts_list = list(map(int, input().split("@")))

cupid_index = 0

while True:

    command = input()

    if command == "Love!":
        break
    else:
        jump_length = int(command.split()[1])
        cupid_index += jump_length

        if cupid_index > len(hearts_list) - 1:
            cupid_index = 0
        hearts_list[cupid_index] -= 2

        if hearts_list[cupid_index] == 0:
            print(f"Place {cupid_index} has Valentine's day.")

        elif hearts_list[cupid_index] < 0:
            print(f"Place {cupid_index} already had Valentine's day.")

failed_places = [heart for heart in hearts_list if heart > 0]

print(f"Cupid's last position was {cupid_index}.")

if len(failed_places) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(failed_places)} places.")


