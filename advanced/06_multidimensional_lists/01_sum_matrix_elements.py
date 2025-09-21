rows, columns = map(int, input().split(", "))
matrix = []
total_sum = 0
for _ in range(rows):
    current_list = list(map(int, input().split(", ")))
    total_sum += sum(current_list)
    matrix.append(current_list)

print(total_sum)
print(matrix)