rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
primary_diagonal = []
secondary_diagonal = []
x = rows - 1
for i in range(rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][x])
    x -= 1

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")