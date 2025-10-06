presents_count = int(input())
n = int(input())

matrix = []
santa_location = []
naughty_kids = []
nice_kids = []
cookies = []
directions_dict = {"right": [0, 1],
                   "left": [0, -1],
                   "up": [-1, 0],
                   "down": [1, 0]}
happy_kids = 0

for row_i in range(n):
    matrix.append(input().split())
    for col_i in range(n):
        if matrix[row_i][col_i] == "S":
            santa_location = [row_i, col_i]
        elif matrix[row_i][col_i] == "X":
            naughty_kids.append([row_i, col_i])
        elif matrix[row_i][col_i] == "V":
            nice_kids.append([row_i, col_i])
        elif matrix[row_i][col_i] == "C":
            cookies.append([row_i, col_i])

while (command := input()) != "Christmas morning":
    current_row, current_col = santa_location
    desired_row = current_row + directions_dict[command][0]
    desired_col = current_col + directions_dict[command][1]
    desired_location = [desired_row, desired_col]

    # do actions
    # nice kid case
    if nice_kids and desired_location in nice_kids:
        nice_kids.remove(desired_location)
        happy_kids += 1
        presents_count -= 1

    # cookie case
    elif desired_location in cookies:
        for coordinates in directions_dict.values():
            c_row, c_col = desired_location
            d_row = c_row + coordinates[0]
            d_col = c_col + coordinates[1]
            d_location = [d_row, d_col]
            if d_location in nice_kids:
                nice_kids.remove(d_location)
                happy_kids += 1
                presents_count -= 1
            elif d_location in naughty_kids:
                naughty_kids.remove(d_location)
                presents_count -= 1
            matrix[d_row][d_col] = "-"
            if presents_count == 0:
                break

    # santa moves
    matrix[current_row][current_col] = "-" # mark his last location as empty
    matrix[desired_row][desired_col] = "S" # mark his current location as S
    santa_location = desired_location.copy() # set his current location

    # break if out of presents
    if presents_count == 0:
        break

success = False
if not nice_kids:
    success = True

if presents_count == 0 and not success:
    print("Santa ran out of presents!")
for row in matrix:
    print(" ".join(row))
if success:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids)} nice kid/s.")


