import numba as nb



win_masks = (
    0b111000000,
    0b000111000,
    0b000000111,
    0b100100100,
    0b010010010,
    0b001001001,
    0b100010001,
    0b001010100
)


@nb.njit(inline='always')
def eval_board(x_board, o_board):
    for mask in win_masks:
        if x_board & mask == mask:
            return 1
        if o_board & mask == mask:
            return -1

    if x_board | o_board == 0b111111111:
        return 0

    return 2
