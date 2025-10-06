n = int(input())

matrix = []
alice_position = []
rabbit_position = []
collected_eggs = 0
leave_indexing_loop = False

for row_i in range(n):
    matrix.append(input().split())
    for col_i in range(n):
        if matrix[row_i][col_i] == "A":
            alice_position = [row_i, col_i]
            matrix[row_i][col_i] = "*"
        elif matrix[row_i][col_i] == "R":
            rabbit_position = (row_i, col_i)

while True:
    command = input()

    # movements
    # change row
    if command == "up":
        alice_position[0] -= 1

        if alice_position[0] < 0:
            print("Alice didn't make it to the tea party.")
            break

    elif command == "down":
        alice_position[0] += 1

        if alice_position[0] == n:
            print("Alice didn't make it to the tea party.")
            break

    # change column
    elif command == "left":
        alice_position[1] -= 1

        if alice_position[1] < 0:
            print("Alice didn't make it to the tea party.")
            break

    elif command == "right":
        alice_position[1] += 1

        if alice_position[1] == n:
            print("Alice didn't make it to the tea party.")
            break

    # situation handling - Alice has made her move
    alice_row, alice_column = alice_position

    # rabbit case
    if alice_row == rabbit_position[0] and alice_column == rabbit_position[1]:
        matrix[alice_row][alice_column] = "*"
        print("Alice didn't make it to the tea party.")
        break

    # collecting case
    elif matrix[alice_row][alice_column].isdecimal():
        collected_eggs += int(matrix[alice_row][alice_column])

    # empty case is handled on its own - just mark her path
    matrix[alice_row][alice_column] = "*"

    # check at the end of the loop if alice has collected the eggs
    if collected_eggs >= 10:
        print("She did it! She went to the party.")
        break

# print the final matrix
for row in matrix:
    print(" ".join(row))
