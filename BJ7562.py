import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    data = [[0 for _ in range(n)] for _ in range(n)]
    s = list(map(int, sys.stdin.readline().split()))
    e = list(map(int, sys.stdin.readline().split()))

    q = deque()
    q.append(s)
    sum = [[0 for _ in range(n)] for _ in range(n)]
    dx = [2, 2, 1, 1, -1, -1, -2, -2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    while q:
        cor = q.popleft()
        x = cor[0]
        y = cor[1]

        if x == e[0] and y == e[1]:
            break

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and data[new_y][new_x] == 0:
                data[new_y][new_x] = 1
                sum[new_y][new_x] = sum[y][x] + 1
                q.append([new_x, new_y])

    print(sum[e[1]][e[0]])
