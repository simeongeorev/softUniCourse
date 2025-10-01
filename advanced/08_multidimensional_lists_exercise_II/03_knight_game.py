n = int(input())
chess_board = [list(input()) for _ in range(n)]

deleted_ks = 0
possible_moves = ((-2, 1), (-1, 2),
                  (1, 2), (2, 1),
                  (2, -1), (1, -2),
                  (-1, -2), (-2, -1))

knights_powers = [1, 1]
while sum(knights_powers) != 0:

    ks_indexes = []

    for row_i in range(n):
        for col_i in range(n):
            if chess_board[row_i][col_i] == "K":
                ks_indexes.append([row_i, col_i])

    knights_powers.clear()

    for knight in ks_indexes:
        valid_targets = 0
        knight_row = knight[0]
        knight_col = knight[1]
        for move in possible_moves:
            move_row = move[0]
            move_col = move[1]
            check_row = knight_row + move_row
            check_col = knight_col + move_col
            current_check = [check_row, check_col]
            if current_check in ks_indexes:
                valid_targets += 1
        knights_powers.append(valid_targets)

    strongest_k = 0
    strongest_index = 0
    for i in range(len(knights_powers) - 1, -1, -1):
        if knights_powers[i] >= strongest_k:
            strongest_k = knights_powers[i]
            strongest_index = i
    row_del, col_del = ks_indexes[strongest_index]
    chess_board[row_del][col_del] = "0"
    if strongest_k > 0:
        deleted_ks += 1

print(deleted_ks)
