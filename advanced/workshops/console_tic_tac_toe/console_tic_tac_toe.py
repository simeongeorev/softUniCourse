import math

X_SIGN = 'X'
O_SIGN = 'O'


def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")

    while True:
        player_one_sign = input(f"{player_one_name} would you like to play with "
                                f"'{X_SIGN}' or '{O_SIGN}'? ").strip().upper()
        if player_one_sign not in [X_SIGN.upper(), O_SIGN.upper()]:
            print("ERROR: Invalid symbol.\nPlease choose a valid symbol.")
            continue
        break

    player_two_sign = 'X' if player_one_sign == 'O' else 'O'
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print(f"{player_one_name} starts first!")


def play(current, board):
    while True:
        choice = input(f"{current[0]} choose a free position [1-9]: ")

        if not choice.isnumeric():
            print("ERROR: Incorrect position entered.\n"
                  "Please enter a numeric position from [1-9].")
            continue

        choice = int(choice)
        if choice not in range(1, 10):
            print("ERROR: Position entered out of range [1-9].\n"
                  "Please enter a position from [1-9].")
            continue

        row = math.ceil(choice / 3) - 1
        col = choice % 3 - 1

        if board[row][col] != " ":
            print("ERROR: The chosen position has already been marked.\n"
                  "Please try again with a free position.")
            continue

        break

    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)


def draw_board(board):
    for row in board:
        print('| ', end='')
        print(' | '.join([str(x) for x in row]), end="")
        print(' |')


def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])

    first_col = all([x == current[1] for x in
                     [board[0][0], board[1][0], board[2][0]]])
    second_col = all([x == current[1] for x in
                      [board[0][1], board[1][1], board[2][1]]])
    third_col = all([x == current[1] for x in
                     [board[0][2], board[1][2], board[2][2]]])

    main_diagonal = all([x == current[1] for x in
                         [board[0][0], board[1][1], board[2][2]]])
    second_diagonal = all([x == current[1] for x in
                           [board[0][2], board[1][1], board[2][0]]])

    win = any([first_row, second_row, third_row,
               first_col, second_col, third_col, main_diagonal, second_diagonal])
    if win:
        print(f"{current[0]} won!")
        loop = False

    empty_spaces_left = any([x == " " for row in board for x in row])
    if not empty_spaces_left:
        print("Game over!\nIt's a tie!")
        loop = False


player_one = None
player_two = None
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
setup()
current = player_one
other = player_two
loop = True

while loop:
    play(current, board)
    current, other = other, current
