N = int(input())

BEE_SYMBOL = "B"
HIVE_SYMBOL = "H"
EMPTY_SPACE = "-"
REQUIRED_NECTAR = 30

matrix = []
current_position = None
energy = 15
collected_nectar = 0
directions_dict = {"right": (0, 1),
                   "left": (0, -1),
                   "up": (-1, 0),
                   "down": (1, 0)}
revival_used = False
hive_reached = False

for row_i in range(N):
    matrix.append(list(input()))
    if BEE_SYMBOL in matrix[row_i]:
        current_position = [row_i, matrix[row_i].index(BEE_SYMBOL)]


def move_bee(c_row, c_col, n_row, n_col):
    matrix[n_row][n_col] = BEE_SYMBOL
    matrix[c_row][c_col] = EMPTY_SPACE
    return [n_row, n_col]


while True:
    command = input()

    # spend energy for the turn
    energy -= 1

    current_row, current_col = current_position
    next_row = current_row + directions_dict[command][0]
    next_col = current_col + directions_dict[command][1]

    if next_row not in range(0, N) or next_col not in range(0, N):
        if next_row < 0:
            next_row = N - 1
        elif next_row > N - 1:
            next_row = 0
        elif next_col < 0:
            next_col = N - 1
        elif next_col > N - 1:
            next_col = 0

    if matrix[next_row][next_col].isdigit():
        collected_nectar += int(matrix[next_row][next_col])
        current_position = move_bee(current_row, current_col, next_row, next_col)


    elif matrix[next_row][next_col] == "-":
        current_position = move_bee(current_row, current_col, next_row, next_col)


    elif matrix[next_row][next_col] == HIVE_SYMBOL:
        current_position = move_bee(current_row, current_col, next_row, next_col)
        hive_reached = True
        break

    if energy <= 0:
        if collected_nectar >= REQUIRED_NECTAR and revival_used is False:
            energy += (collected_nectar - REQUIRED_NECTAR)
            collected_nectar = REQUIRED_NECTAR
            revival_used = True
            if energy <= 0:
                break
        else:
            break

if not hive_reached:
    print("This is the end! Beesy ran out of energy.")
elif collected_nectar >= 30:
    print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
elif collected_nectar < 30:
    print("Beesy did not manage to collect enough nectar.")

for row in matrix:
    print(''.join(row))
