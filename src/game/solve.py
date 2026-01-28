import numba as nb

from game.game_utils import eval_board



@nb.njit
def create_table_3x3(x_board, o_board, player, table):
    # Checks if answer is already in table
    if (x_board, o_board) in table:
        return table[x_board, o_board][0]

    # Returns winner or draw if there is one
    curr_pos_eval = eval_board(x_board, o_board)
    if curr_pos_eval != 2:
        return curr_pos_eval

    # -1 = opponent wins, 0 = draw, 1 = player wins
    status = -player
    play_bit = 0
    playable = x_board | o_board

    for i in range(9):
        # Exits if spot is full
        bit = (1 << i)
        if playable & bit != 0:
            continue

        # Recursively makes the table
        if player == 1:
            result = create_table_3x3(x_board | bit, o_board, -player, table)
        else:
            result = create_table_3x3(x_board, o_board | bit, -player, table)

        # Victory marking
        if result == player:
            status = player
            play_bit = bit
        elif result == 0 and status == -player:
            status = 0
            play_bit = bit
        elif result == -player and status == -player:
            status = -player
            play_bit = bit

    # Records the results of the search
    table[x_board, o_board] = (status, play_bit)
    return status
