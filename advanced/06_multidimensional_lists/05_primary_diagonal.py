rows = int(input())
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

primary_sum = 0
for i in range(rows):
    primary_sum+= matrix[i][i]

print(primary_sum)