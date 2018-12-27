""" n parameter can be found from the board """

''' the funtion tests if the cells have an adjacents cells of same values '''


def has_adjacent_tile(board, x, y):
    adjacent = False
    n = len(board)
    value = board[x][y]
    xUp, xDown = x - 1, x + 1
    yLeft, yRight = y - 1, y + 1

    if xUp < 0:
        xUp = 0

    if xDown > n - 1:
        xDown = n - 1

    if yRight > n - 1:
        yRight = n - 1

    if yLeft < 0:
        yLeft = 0

    if xUp != x:
        if board[xUp][y] == value:
            adjacent = True
    if xDown != x:
        if board[xDown][y] == value:
            adjacent = True
    if yLeft != y:
        if board[x][yLeft] == value:
            adjacent = True
    if yRight != y:
        if board[x][yRight] == value:
            adjacent = True

    return adjacent


''' the function tests if the shot still playable on the grid '''


def is_move_available(board, x, y):
    for i in range(len(board)):
        for j in range(len(board)):
            if has_adjacent_tile(board, x, y) == False:
                print("no move still playable")
                return False
            return True


''' returns the max value of te given board '''


def get_max_board_value(board):
    max = 1
    for line in board:
        for item in line:
            if item > max:
                max = item

    return max
