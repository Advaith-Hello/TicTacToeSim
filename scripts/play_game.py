from game.json_utils import load_numba_dict
from game.game_utils import eval_board
from game.board import Board3x3



lookup_table = load_numba_dict("../data/lookup_table.json")
curr_board = Board3x3()
print(curr_board)

while True:
    try:
        col = int(input("Col (0-2): "))
        row = int(input("Row (0-2): "))
        if curr_board.board[row][col] != " ":
            print("Spot taken. Try again.")
            continue
        curr_board.board[row][col] = "X"
    except (ValueError, IndexError):
        print("Inputs are: 0, 1, or 2.")
        continue

    curr_bin = curr_board.bin()
    status = eval_board(*curr_bin)

    if status != 2:
        print(curr_bin)
        print("X wins" if status == 1 else "Draw")
        break

    if curr_bin not in lookup_table:
        print(curr_bin)
        print("Draw")
        break

    move_mask = lookup_table[curr_bin][1]
    ans = move_mask.bit_length() - 1
    curr_board.board[ans // 3][ans % 3] = "O"
    curr_bin = curr_board.bin()
    print(curr_board)

    status = eval_board(*curr_bin)
    if status != 2:
        print("Draw" if status == 0 else "O wins")
        break
