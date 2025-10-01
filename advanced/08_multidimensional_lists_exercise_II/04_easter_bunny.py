n = int(input())
matrix = []
BUNNY = "B"
TRAP = "X"
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

bunny_row, bunny_column = None, None

for row_i in range(n):
    matrix.append(input().split())
    for col_i in range(n):
        if matrix[row_i][col_i] == BUNNY:
            bunny_row = row_i
            bunny_column = col_i

# storing the results
results_dict = {UP: [],
                DOWN: [],
                LEFT: [],
                RIGHT: []}

counts_dict = {}

# UP
if bunny_row != 0:
    for row_i in range(bunny_row - 1, -1, -1):
        # if X we break
        if matrix[row_i][bunny_column] == TRAP:
            break
        else:
            results_dict[UP].append([row_i, bunny_column])
            if UP not in counts_dict.keys():
                counts_dict[UP] = int(matrix[row_i][bunny_column])
            else:
                counts_dict[UP] += int(matrix[row_i][bunny_column])

# DOWN
last_row_i = n - 1
if bunny_row != last_row_i:
    for row_i in range(bunny_row + 1, n):
        # if X we break
        if matrix[row_i][bunny_column] == TRAP:
            break
        else:
            results_dict[DOWN].append([row_i, bunny_column])
            if DOWN not in counts_dict.keys():
                counts_dict[DOWN] = int(matrix[row_i][bunny_column])
            else:
                counts_dict[DOWN] += int(matrix[row_i][bunny_column])

# LEFT
if bunny_column != 0:
    for col_i in range(bunny_column - 1, -1, -1):
        # if X we break
        if matrix[bunny_row][col_i] == TRAP:
            break
        else:
            results_dict[LEFT].append([bunny_row, col_i])
            if LEFT not in counts_dict.keys():
                counts_dict[LEFT] = int(matrix[bunny_row][col_i])
            else:
                counts_dict[LEFT] += int(matrix[bunny_row][col_i])

# RIGHT
last_col_i = n - 1
if bunny_column != last_col_i:
    for col_i in range(bunny_column + 1, n):
        # if X we break
        if matrix[bunny_row][col_i] == TRAP:
            break
        else:
            results_dict[RIGHT].append([bunny_row, col_i])
            if RIGHT not in counts_dict.keys():
                counts_dict[RIGHT] = int(matrix[bunny_row][col_i])
            else:
                counts_dict[RIGHT] += int(matrix[bunny_row][col_i])

best_path, total_score = sorted(counts_dict.items(), key=lambda x: -x[1]).__getitem__(0)

print(best_path)
for position in results_dict[best_path]:
    print(position)
print(total_score)
