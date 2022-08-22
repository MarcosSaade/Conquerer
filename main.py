import math
import random
from static_eval import *

board = [
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ']
]

turn = random.choice((0, 1))


def greet():
    print("----------------------------------------------------"
          "\n   _____                                           "
          "\n  / ___|___  _ __   __ _ _   _  ___ _ __ ___ _ __"
          "\n | |   / _ \| '_ \ / _` | | | |/ _ \ '__/ _ \ '__|"
          "\n | |__| (_) | | | | (_| | |_| |  __/ | |  __/ |"
          "\n \____\___/|_| |_|\__, |\__,_|\___|_|  \___|_|"
          "\n                    |_|                         "
          "\n ---------------------------------------------------- \n\n")
    print(
        'The game presents a 4x4 grid.'
        '\n\nThe player who "conquers" the most 2x2 squares wins.'
        '\n\nA square is conquered by placing 3 or more of your pieces in it.'
        '\n\nYou can play against an AI, or watch two AIs play themselves. \n\n'
    )


def draw():
    print('\n' * 25)

    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])


def get_turn(t):
    turn = 0 if t else 1

    return turn


def select_move():
    i = int(input('row: '))
    j = int(input('col: '))

    while 0 < i > 3:
        print('Please select number from 0-3')
        i = int(input('row: '))
        j = int(input('col: '))

    place(i, j, o)


def place(i, j, shape):
    if board[i][j] == ' ':
        board[i][j] = shape
        draw()
    else:
        select_move()


def is_full():
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2] and ' ' not in board[3]:
        return True


def get_score(hero, villain):
    score = 0

    squares = [
        [board[0][0], board[0][1], board[1][0], board[1][1]],
        [board[0][1], board[0][2], board[1][1], board[1][2]],
        [board[0][2], board[0][3], board[1][2], board[1][3]],
        [board[1][0], board[1][1], board[2][0], board[2][1]],
        [board[1][1], board[1][2], board[2][1], board[2][2]],
        [board[1][2], board[1][3], board[2][2], board[2][3]],
        [board[2][0], board[2][1], board[3][0], board[3][1]],
        [board[2][1], board[2][2], board[3][1], board[3][2]],
        [board[2][2], board[2][3], board[3][2], board[3][3]],
    ]

    for square in squares:
        if square.count(hero) >= 3:
            score += 1
        if square.count(villain) >= 3:
            score -= 1

    return score


def ai(depth, hero, villain):
    best_score = -math.inf

    for i in range(4):
        for j in range(4):
            if board[i][j] == ' ':
                available_move = [i, j]
                board[i][j] = hero
                score = minimax(board, depth, -math.inf, math.inf, False, hero, villain)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = [i, j]

    if 'best_move' not in locals():
        best_move = available_move

    board[best_move[0]][best_move[1]] = hero
    draw()


def minimax(board, depth, alpha, beta, is_max, hero, villain):
    if depth == 0:
        return static_eval(board, hero, villain)

    score = get_score(hero, villain)
    if is_full():
        return score

    if is_max:
        best_score = -math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == ' ':
                    board[i][j] = hero
                    score = minimax(board, depth - 1, alpha, beta, False, hero, villain)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(4):
            for j in range(4):
                if board[i][j] == ' ':
                    board[i][j] = villain
                    score = minimax(board, depth - 1, alpha, beta, True, hero, villain)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score


greet()

x = '\u2726'
o = '\u2742'


def init():
    increment = 0

    human = int(input('\n Type 1 for play, 0 for auto: '))

    depth_o = 6

    if human == 0:
        depth_x = 6
    else:
        print(f'You are {o} \n')

        level = int(input('Choose difficulty: 1 = easy, 2 = medium, 3 = hard: '))

        if level == 1:
            depth_x = 1
        elif level == 2:
            depth_x = 3
        else:
            depth_x = 6

    draw()

    return increment, depth_x, depth_o, human


increment, depth_x, depth_o, human = init()

playing = True

while playing:
    if not is_full():
        turn = get_turn(turn)
        if turn == 0:
            if human:
                select_move()
            else:
                depth_o += increment
                ai(depth_o, hero=o, villain=x)
        else:
            ai(depth_x, hero=x, villain=o)
            depth_x += increment
            increment += 1

        print(f'Score: {get_score(o, x)}')
    else:
        if get_score(o, x) > 0:
            print(f'{o} wins')
        elif get_score(o, x) == 0:
            print('tie')
        else:
            print(f'\n {x} wins!')

        playing = int(input('\n Play again? 1 = yes, 0 = no: '))

        board = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]

        turn = random.choice((0, 1))

        increment, depth_x, depth_o, human = init()

