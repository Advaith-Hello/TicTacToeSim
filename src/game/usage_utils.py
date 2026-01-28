def table_to_bin(board):
    x_board = 0
    o_board = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] in [1, "X", "x"]:
                x_board |= 1 << (3 * i + j)
            elif board[i][j] in [-1, "O", "o"]:
                o_board |= 1 << (3 * i + j)

    return x_board, o_board

