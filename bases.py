from random import random

''' returns number between 1 and 4 based on given probability '''


def get_random_number(proba):
    number = random()

    p1 = proba[0]
    p2 = proba[1]
    p3 = proba[2]

    if 0 <= number <= p1:
        return 4

    if p1 < number <= p2:
        return 3

    if p2 < number <= p3:
        return 2

    if p3 < number <= 1:
        return 1


''' this function returns a list with two dimensions '''


def get_random_board(n, proba):
    board = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(get_random_number(proba))
            continue

        board.append(tmp)
    return board


''' this function displays the precedent list on the board  '''


def display(board):
    for line in board:
        for item in line:
            print(item, ' ', end='')

        print('\n')
    print('*******************************')
    print('\n')
    print('*******************************')
    print('\n')
