from collections import deque

rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

while (command := input()) != "END":
    command = deque(command.split())
    if len(command) != 5 or command[0] != "swap":
        print("Invalid input!")
        continue

    swap_word = command.popleft()
    coordinates = [int(x) for x in command]

    if not all(x >= 0 for x in coordinates):
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = coordinates
    if row1 >= rows or row2 >= rows or col1 >= cols or col2 >= cols:
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for sub_list in matrix:
        print(*sub_list, sep=" ")