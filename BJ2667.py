import sys
from collections import deque


def init():
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                return i, j

    return -1, -1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    data = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
    idx = 0
    res = list()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while True:
        y, x = init()
        if y == -1 and x == -1:
            break
        else:
            q = deque()
            q.append([y, x])
            count = 0
            while q:
                c = q.popleft()
                y = c[0]
                x = c[1]
                if 0 <= x < n and 0 <= y < n and data[y][x] == 1:
                    data[y][x] = 0
                    count += 1
                    for i in range(4):
                        new_y = y + dy[i]
                        new_x = x + dx[i]
                        if 0 <= new_x < n and 0 <= new_y < n and data[new_y][new_x] == 1:
                            q.append([new_y, new_x])

            res.append(count)
            idx += 1

    print(idx)
    res.sort()
    print(*res, sep="\n")


