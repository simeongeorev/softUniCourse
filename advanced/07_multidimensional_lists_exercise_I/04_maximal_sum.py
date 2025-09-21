import math

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

grid_sum = -math.inf
largest_grid = []

for i in range(rows - 2):
    for j in range(cols - 2):
        three_by_three = [
            [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]],
             [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]],
             [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]],
        ]
        current_sum = 0
        for row in three_by_three:
            current_sum += sum(row)
        if current_sum > grid_sum:
            grid_sum = current_sum
            largest_grid = three_by_three

print(f"Sum = {grid_sum}")
for row in largest_grid:
    print(*row)

