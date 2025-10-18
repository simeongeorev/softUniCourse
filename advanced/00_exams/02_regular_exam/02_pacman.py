PACMAN_SIGN = "P"
STAR_SIGN = "*"
GH0ST_SIGN = "G"
EMPTY_SIGN = "-"
FREEZER_SIGN = "F"

N = int(input())

matrix = []
current_position = None
stars_count = 0

for row_i in range(N):
    matrix.append(list(input()))

    if PACMAN_SIGN in matrix[row_i]:
        current_position = [row_i, matrix[row_i].index(PACMAN_SIGN)]

    stars_count += matrix[row_i].count(STAR_SIGN)

directions_dict = {"right": (0, 1),
                   "left": (0, -1),
                   "up": (-1, 0),
                   "down": (1, 0)}
hp = 100
is_frozen = False

def move():
    matrix[cur_row][cur_col] = EMPTY_SIGN
    matrix[next_row][next_col] = PACMAN_SIGN
    return [next_row, next_col]

while (command := input()) != "end":

    cur_row, cur_col = current_position
    next_row = cur_row + directions_dict[command][0]
    next_col = cur_col + directions_dict[command][1]
    next_position = [cur_row, cur_col]

    if next_row not in range(0, N) or next_col not in range(0, N):
        if next_row < 0:
            next_row = N - 1
        elif next_row > N - 1:
            next_row = 0

        elif next_col < 0:
            next_col = N - 1
        elif next_col > N - 1:
            next_col = 0

    next_sign = matrix[next_row][next_col]

    # empty position
    if next_sign == EMPTY_SIGN:
        current_position = move()

    # star position
    elif next_sign == STAR_SIGN:
        current_position = move()
        stars_count -= 1
        if stars_count == 0:
            print("Pacman wins! All the stars are collected.")
            break

    # ghost position
    elif next_sign == GH0ST_SIGN:
        current_position = move()

        if is_frozen:
            is_frozen = False
        else:
            hp -= 50
            if hp <= 0:
                print(f"Game over! Pacman last coordinates [{next_row},{next_col}]")
                break

    # freezer position
    elif next_sign == FREEZER_SIGN:
        is_frozen = True
        current_position = move()

else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {hp}")

if stars_count > 0:
    print(f"Uncollected stars: {stars_count}")

for row in matrix:
    print("".join(row))

