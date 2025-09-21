rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append(map(int, input().split(", ")))
    # matrix.extend(input().split(", "))

# flattened_matrix = []
# for row in matrix:
#     for column in row:
#         flattened_matrix.append(column)

matrix = [num for row in matrix for num in row]

print(matrix)