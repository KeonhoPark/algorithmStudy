def solution(keyinput, board):
    x = 0
    y = 0
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    for k in keyinput:
        if k == 'left' and x > -x_limit:
            x -= 1
        elif k == 'right' and x < x_limit:
            x += 1
        elif k == 'up' and y < y_limit:
            y += 1
        elif k == 'down' and y > -y_limit:
            y -= 1

    return [x, y]
