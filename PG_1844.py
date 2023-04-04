from collections import deque


def solution(maps):
    w = len(maps[0])
    h = len(maps)

    q = deque()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q.append([0, 0, 1])
    maps[0][0] = 0

    flag = 0
    while q:
        cor = q.popleft()
        y = cor[0]
        x = cor[1]
        c = cor[2]

        if y == h - 1 and x == w - 1:
            return c

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_y < h and 0 <= new_x < w and maps[new_y][new_x] == 1:
                q.append([new_y, new_x, c + 1])
                maps[new_y][new_x] = 0

    return -1
