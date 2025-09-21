import math

rows, columns = map(int, input().split(", "))
matrix = []
submatrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

submatrix_sum = -math.inf
for row_i in range(rows - 1):
    for col_i in range(columns - 1):
        current_sum = (matrix[row_i][col_i]
                       + matrix[row_i][col_i+1]
                       + matrix[row_i+1][col_i]
                       + matrix[row_i+1][col_i+1])
        if current_sum > submatrix_sum:
            submatrix_sum = current_sum
            submatrix.clear()
            submatrix.append([matrix[row_i][col_i], matrix[row_i][col_i+1]])
            submatrix.append([matrix[row_i+1][col_i], matrix[row_i+1][col_i+1]])

for sub_list in submatrix:
    print(" ".join(str(x) for x in sub_list))

print(submatrix_sum)