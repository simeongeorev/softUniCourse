N = int(input())
board = []

PLAYER_SYM = "P"
STAR_SYM = "*"
OBSTACLE_SYM = "#"

stars_collected = 2
current_coordinates = None

directions_dict = {"right": (0, 1),
                   "left": (0, -1),
                   "up": (-1, 0),
                   "down": (1, 0)}

for row_i in range(N):
    board.append(input().split())
    if PLAYER_SYM in board[row_i]:
        current_coordinates = [row_i, board[row_i].index(PLAYER_SYM)]


def move_player():
    board[new_row][new_col] = PLAYER_SYM
    board[current_row][current_col] = "."
    return [new_row, new_col]


while 0 < stars_collected < 10:
    move_command = input()

    current_row, current_col = current_coordinates
    new_row = current_row + directions_dict[move_command][0]
    new_col = current_col + directions_dict[move_command][1]

    # out of bounds
    if new_row not in range(0, N) or new_col not in range(0, N):
        new_row, new_col = [0, 0]
        if board[new_row][new_col] == STAR_SYM:
            stars_collected += 1
        current_coordinates = move_player()
        continue

    new_coordinates_symbol = board[new_row][new_col]

    # obstacle
    if new_coordinates_symbol == OBSTACLE_SYM:
        stars_collected -= 1
        continue

    # star
    if new_coordinates_symbol == STAR_SYM:
        stars_collected += 1

    current_coordinates = move_player()

if stars_collected == 10:
    print("You won! You have collected 10 stars.")
else:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{current_coordinates[0]}, {current_coordinates[1]}]")

for row in board:
    print(" ".join(row))
