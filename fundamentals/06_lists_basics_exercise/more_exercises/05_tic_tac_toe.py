line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

two_d_list = [line_1, line_2, line_3]

first_player_won = None
counter_verticals_left = 0
counter_verticals_right_1 = 0
counter_verticals_right_2 = 0
minus_y = -1

for x in range(len(two_d_list)):
    counter_columns = 0
    counter_rows = 0

    for y in range(len(two_d_list[x])):
        # columns
        if two_d_list[y][x] == "1":
            counter_columns += 1
        elif two_d_list[y][x] == "2":
            counter_columns -= 1

        # rows
        if two_d_list[x][y] == "1":
            counter_rows += 1
        elif two_d_list[x][y] == "2":
            counter_rows -= 1

        # diagonal top left - bottom right
        if x == y:
            if two_d_list[x][y] == "1":
                counter_verticals_left += 1
            elif two_d_list[x][y] == "2":
                counter_verticals_left -= 1

    # diagonal top right
    if two_d_list[x][minus_y] == "1":
        counter_verticals_right_1 += 1
    elif two_d_list[x][minus_y] == "2":
        counter_verticals_right_2 += 1

    minus_y -= 1

    if (counter_columns == 3
            or counter_rows == 3
            or counter_verticals_left == 3
            or counter_verticals_right_1 == 3):
        first_player_won = True
        break
    if (counter_columns == -3
            or counter_rows == -3
            or counter_verticals_left == -3
            or counter_verticals_right_2 == 3):
        first_player_won = False
        break

if first_player_won:
    print("First player won")
elif first_player_won == False:
    print("Second player won")
elif first_player_won is None:
    print("Draw!")
