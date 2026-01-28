from game.json_utils import load_numba_dict
from game.usage_utils import table_to_bin
from game.game_utils import eval_board


def print_board(x_board, o_board):
    print("-------")
    for r in range(3):
        for c in range(3):
            i = 3 * r + c
            if (x_board >> i) & 1:
                print("X", end=" ")
            elif (o_board >> i) & 1:
                print("O", end=" ")
            else:
                print("_", end=" ")
        print()
    print("-------")


lookup_table = load_numba_dict("../data/lookup_table.json")

curr_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

print_board(*table_to_bin(curr_board))

while True:
    try:
        col = int(input("Col (0-2): "))
        row = int(input("Row (0-2): "))
        if curr_board[row][col] != " ":
            print("Spot taken. Try again.")
            continue
        curr_board[row][col] = "X"
    except (ValueError, IndexError):
        print("Inputs are: 0, 1, or 2.")
        continue

    curr_bin = table_to_bin(curr_board)
    status = eval_board(*curr_bin)

    if status != 2:
        print_board(*curr_bin)
        print("X wins" if status == 1 else "Draw")
        break

    if curr_bin not in lookup_table:
        print_board(*curr_bin)
        print("Draw")
        break

    move_mask = lookup_table[curr_bin][1]
    ans = move_mask.bit_length() - 1
    curr_board[ans // 3][ans % 3] = "O"
    curr_bin = table_to_bin(curr_board)
    print_board(*curr_bin)

    status = eval_board(*curr_bin)
    if status != 2:
        print("Draw" if status == 0 else "O wins")
        break
