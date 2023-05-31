def solution(board):
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, 1, -1]
    count = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in range(len(dx)):
                    new_i = i + dx[k]
                    new_j = j + dy[k]
                    if 0 <= new_i < len(board) and 0 <= new_j < len(board) and board[new_i][new_j] == 0:
                        board[new_i][new_j] = 2

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                count += 1

    return count
