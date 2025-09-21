rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []
x = rows - 1
for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][x])
    x -= 1

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)
