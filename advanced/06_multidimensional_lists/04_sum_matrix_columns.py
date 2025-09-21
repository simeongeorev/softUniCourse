rows, columns = map(int, input().split(", "))
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for col_i in range(columns):
    column_sum = 0
    for row_i in range(rows):
        column_sum += matrix[row_i][col_i]
    print(column_sum)

