import sys
from collections import deque


def init():
    q = deque()
    for a in range(h):
        for i in range(c):
            for j in range(r):
                if data[a][i][j] == 1:
                    q.append([a, i, j])

    return q


def find_zero():
    for a in range(h):
        for i in range(c):
            for j in range(r):
                if data[a][i][j] == 0:
                    return True

    return False


def bfs(q):
    global c
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    while q:
        cor = q.popleft()
        a = cor[0]
        y = cor[1]
        x = cor[2]
        for i in range(6):
            new_h = a + dh[i]
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_y < c and 0 <= new_x < r and 0 <= new_h < h and data[new_h][new_y][new_x] == 0:
                data[new_h][new_y][new_x] = 1
                q.append([new_h, new_y, new_x])
                res[new_h][new_y][new_x] = res[a][y][x] + 1


if __name__ == "__main__":
    r, c, h = map(int, sys.stdin.readline().split())
    data = [[list(map(int, sys.stdin.readline().split())) for _ in range(c)] for _ in range(h)]
    res = [[[0 for _ in range(r)] for _ in range(c)] for _ in range(h)]

    q = init()
    bfs(q)

    if find_zero():
        print(-1)
    else:
        mx = -1
        for a in res:
            for i in range(len(a)):
                tmp = max(a[i])
                if mx < tmp:
                    mx = tmp
        print(mx)
