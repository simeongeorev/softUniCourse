n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

symbol = input()
position_tuple = tuple()
exit_flag = False

for row_i in range(n):
    for col_i in range(n):
        if symbol == matrix[row_i][col_i]:
            position_tuple = (row_i, col_i)
            exit_flag = True
            break
    if exit_flag:
        break

if exit_flag:
    print(f"({', '.join(str(x) for x in position_tuple)})")
else:
    print(f"{symbol} does not occur in the matrix")


