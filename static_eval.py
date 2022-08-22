def static_eval(board, hero, villain):
    eval = 0

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
            eval += 100
        if square.count(villain) >= 3:
            eval -= 100

        if square.count(hero) == 4:
            eval -= 10

        if square.count(hero) == 2 and square.count(' ') == 2:
            eval += 70
        if square.count(villain) == 2 and square.count(' ') == 2:
            eval -= 70

    return eval
