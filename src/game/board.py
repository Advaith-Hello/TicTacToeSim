class Board3x3:
    def __init__(self, board=None):
        if board is None:
            self.board = [[" "] * 3 for _ in range(3)]
        else:
            self.board = board

    def __str__(self):
        x_board, o_board = self.bin()
        txt = "-------\n"
        for r in range(3):
            txt += " "
            for c in range(3):
                i = 3 * r + c
                if (x_board >> i) & 1:
                    txt += "X"
                elif (o_board >> i) & 1:
                    txt += "O"
                else:
                    txt += "_"
                txt += " "
            txt += "\n"

        return txt + "-------"

    def bin(self):
        x_board = 0
        o_board = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] in [1, "X", "x"]:
                    x_board |= 1 << (3 * i + j)
                elif self.board[i][j] in [-1, "O", "o"]:
                    o_board |= 1 << (3 * i + j)

        return x_board, o_board
