cake_width = int(input())
cake_height = int(input())

pieces_total = cake_height * cake_width
pieces_of_cake_taken = 0

command = input()

while command != "STOP":
    pieces_of_cake_taken += int(command)

    if pieces_of_cake_taken >= pieces_total:
        print(f"No more cake left! You need {pieces_of_cake_taken - pieces_total} pieces more.")
        break

    command = input()

else:
    print(f"{pieces_total - pieces_of_cake_taken} pieces are left.")