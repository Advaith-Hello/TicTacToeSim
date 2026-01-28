import numba as nb

from game.game_utils import eval_board



@nb.njit
def solve_3x3(x_board, o_board, player, table):
    # Checks if answer is already in table
    if (x_board, o_board) in table:
        return table[x_board, o_board][0]

    # Returns winner or draw if there is one
    curr_pos_eval = eval_board(x_board, o_board)
    if curr_pos_eval != 2:
        return curr_pos_eval

    # Defines the variables used
    opp_bit = 0
    draw_bit = 0
    draw = 0
    playable = x_board | o_board

    for i in range(9):
        # Exits if spot is full
        bit = (1 << i)
        if playable & bit != 0:
            continue

        # Recursively finds the winner of the move
        if player == 1:
            result = solve_3x3(x_board | bit, o_board, -player, table)
        else:
            result = solve_3x3(x_board, o_board | bit, -player, table)

        if result == player: # Player wins
            table[x_board, o_board] = (result, bit)
            return player
        if result == 0: # Draw is marked possible
            draw_bit = bit
            draw = 1
        else:
            opp_bit = bit

    # Draws the game if possible, if not it loses
    if draw == 1:
        table[x_board, o_board] = (0, draw_bit)
        return 0

    table[x_board, o_board] = (-player, opp_bit)
    return -player
