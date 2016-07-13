def heuristica(state):
    n = 0
    if state.utility != 0:
        return state.utility * 10000
    else:
        for move in state.moves:
            n -= value(state.board, move, 'O')
            n += value(state.board, move, 'X')

        return n


def value(board, move, player):
    n= (k_in_row(board, move, player, (0, 1)) +
        k_in_row(board, move, player, (1, 0)) +
        k_in_row(board, move, player, (1, 1)) +
        k_in_row(board, move, player, (1, -1)))
    return n

def k_in_row(board, move, player, (delta_x, delta_y)):
    x, y = move
    n = 0  # n is number of moves in row
    while board.get((x, y)) == player or board.get((x, y)) ==  None:
        if (board.get((x, y)) == player):
            n += 1
        x, y = x + delta_x, y + delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) == None:
        if (board.get((x, y)) == player):
            n += 1
        x, y = x - delta_x, y - delta_y
        if x > 7 or x < 0 or y > 6 or y < 0:
            break

    return n
