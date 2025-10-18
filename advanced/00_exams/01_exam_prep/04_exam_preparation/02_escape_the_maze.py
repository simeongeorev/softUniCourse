N = int(input())
TRAVELER_SIGN = "P"
EXIT_SIGN = "X"
MONSTER_SIGN = "M"
HEALTH_POTION_SIGN = "H"
EMPTY_SPACE_SIGN = "-"

field = []
current_position = None

for row_i in range(N):
    field.append(list(input()))
    if TRAVELER_SIGN in field[row_i]:
        current_position = [row_i, field[row_i].index(TRAVELER_SIGN)]

hp = 100
directions_dict = {"right": [0, 1],
                   "left": [0, -1],
                   "up": [-1, 0],
                   "down": [1, 0]}


def move_traveler(cur_row, cur_col, next_row, next_col):
    field[cur_row][cur_col] = EMPTY_SPACE_SIGN
    field[next_row][next_col] = TRAVELER_SIGN
    return [next_row, next_col]


while True:
    command = input()

    cur_row, cur_col = current_position
    next_row = cur_row + directions_dict[command][0]
    next_col = cur_col + directions_dict[command][1]
    next_position = [next_row, next_col]

    # traveler gets out of bounds
    if next_row not in range(0, N) or next_col not in range(0, N):
        continue

    next_sign = field[next_row][next_col]

    if next_sign == EMPTY_SPACE_SIGN:
        current_position = move_traveler(cur_row, cur_col, next_row, next_col)

    elif next_sign == MONSTER_SIGN:
        hp -= 40

        if hp <= 0:  # traveler dies
            hp = 0
            current_position = move_traveler(cur_row, cur_col, next_row, next_col)
            break
        else:
            current_position = move_traveler(cur_row, cur_col, next_row, next_col)

    elif next_sign == HEALTH_POTION_SIGN:
        hp += 15

        if hp > 100:
            hp = 100

        current_position = move_traveler(cur_row, cur_col, next_row, next_col)

    elif next_sign == EXIT_SIGN:
        current_position = move_traveler(cur_row, cur_col, next_row, next_col)
        break

if hp > 0:
    print("Player escaped the maze. Danger passed!")
else:
    print("Player is dead. Maze over!")

print(f"Player's health: {hp} units")

for row in field:
    print("".join(row))
