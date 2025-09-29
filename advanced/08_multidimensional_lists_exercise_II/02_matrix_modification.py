n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

matrix_str = ""

while (command := input()) != "END":
    command_list = command.split()
    task = command_list[0]
    row = int(command_list[1])
    col = int(command_list[2])
    value = int(command_list[3])

    if row < 0 or row >= len(matrix):
        print("Invalid coordinates")
        continue

    invalid_coordinate = False
    for row_i in matrix:
        if col < 0 or col >= len(row_i):
            print("Invalid coordinates")
            invalid_coordinate = True
            break
    if invalid_coordinate:
        continue

    if task == "Add":
        matrix[row][col] += value
    elif task == "Subtract":
        matrix[row][col] -= value

for row in matrix:
    matrix_str += " ".join([str(x) for x in row])
    matrix_str += "\n"

print(matrix_str)

