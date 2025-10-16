N_ROWS = 6
ERROR_INVALID_ENTRY = "ERROR: The input must be a number [1-7]"

player_one = 1
player_two = 2

current_player = player_one
current_row = 5

board = []
for row_i in range(N_ROWS):
    board.append(list(7 * "0"))


def setup():
    while True:
        selected_col = input(f"Player {current_player},"
                             f" please choose a column").strip()

        if not selected_col.isnumeric():
            print(ERROR_INVALID_ENTRY)
            continue

        selected_col = int(selected_col) - 1

        if selected_col not in range(0, 7):
            print(ERROR_INVALID_ENTRY)
            continue

        # todo add a check if the board is already full

        break
    return selected_col


def check_if_game_is_over(current, board: list):
    continue_game = True

    # horizontal check
    for row_i in range(N_ROWS - 1, -1, -1):
        if board[row_i].count(current) == 4:
            continue_game = False
            break

    # vertical check
    for

    # main diagonals check

    # reverse diagonals check


while True:
    selected_col = setup()
    if board[current_row][selected_col] == "0":
        board[current_row][selected_col] = current_player
    else:
        next_row = current_row - 1
        while True:
            if board[next_row][selected_col] != "0":
                if next_row > 0:
                    next_row = current_row - 1
                    continue
                else:
                    print("ERROR: This column is full."
                          "Select a different one with empty spaces")
                    selected_col = setup()
                    continue

            board[next_row][selected_col] = current_player
            break

    if all(x != "0" for x in board[current_row]):
        current_row -= 1

    check_if_game_over()
    current_player = player_two if current_player == player_one else player_one

print(board)
