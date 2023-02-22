import sys
from collections import deque

c, r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(c)]
count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append([0, 0])
data[0][0] = 0

while True:
    flag = 0

    for a in range(len(q)):
        cor = q.popleft()
        y = cor[0]
        x = cor[1]

        if y == c - 1 and x == r - 1:
            flag = 1
            break

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0 <= new_y < c and 0 <= new_x < r and data[new_y][new_x] == 1:
                q.append([new_y, new_x])
                data[new_y][new_x] = 0

    count += 1

    if flag == 1:
        break

print(count)
