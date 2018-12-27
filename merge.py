from bases import *

""" returns a t-uple of coordinates of adjacents cells of same values """


def get_adjacent_tiles(board, adj_list, x, y):
    if [x, y] not in adj_list:
        adj_list.append([x, y])

    n = len(board)
    value = board[x][y]

    xUp, xDown = x - 1, x + 1
    yLeft, yRight = y - 1, y + 1

    if xUp >= 0 and board[xUp][y] == value and [xUp, y] not in adj_list:
        adj_list.append([xUp, y])
        get_adjacent_tiles(board, adj_list, xUp, y)

    if xDown < n and board[xDown][y] == value and [xDown, y] not in adj_list:
        adj_list.append([xDown, y])
        get_adjacent_tiles(board, adj_list, xDown, y)

    if yLeft >= 0 and board[x][yLeft] == value and [x, yLeft] not in adj_list:
        adj_list.append([x, yLeft])
        get_adjacent_tiles(board, adj_list, x, yLeft)

    if yRight < n and board[x][yRight] == value and [x, yRight] not in adj_list:
        adj_list.append([x, yRight])
        get_adjacent_tiles(board, adj_list, x, yRight)

    return adj_list


board = get_random_board(5, (0.1, 0.2, 0.3))
display(board)
print(get_adjacent_tiles(board, [], 0, 4))

""" when the player click on the cell , all cells of same value become 0"""


def modification(board, x, y):
    display(board)
    adj_list = get_adjacent_tiles(board, [], x, y)

    if len(adj_list) <= 1:
        return

    for item in adj_list:

        if [x, y] != item:
            board[item[0]][item[1]] = 0
        else:
            board[x][y] += 1


""" Fall by gravity the cells located above cells whose value is equal to 0.Finally, it will fill incomplete columns """


def gravity(board, proba):
    for i in range(1, len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                for k in range(i, 0, -1):
                    board[k][j] = board[k - 1][j]
                    board[k - 1][j] = 0

    for i in range(len(board) - 1, -1, - 1):
        for j in range(len(board) - 1, -1, -1):
            if board[i][j] == 0:
                board[i][j] = get_random_number(proba)
