import sys
from collections import deque

c, r = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().strip())) for _ in range(c)]
res = [[[0 for _ in range(2)] for _ in range(r)] for _ in range(c)]
res[0][0][0] = 1
q = deque()
q.append([0, 0, 0])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
print(res)

while q:
    cor = q.popleft()
    y = cor[0]
    x = cor[1]
    is_crashed = cor[2]

    if y == c - 1 and x == r - 1:
        break

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < c and 0 <= new_x < r:
            if data[new_y][new_x] == 0 and res[new_y][new_x][is_crashed] == 0:
                res[new_y][new_x][is_crashed] = res[y][x][is_crashed] + 1
                q.append([new_y, new_x, is_crashed])
                print(res)
                print()
            elif data[new_y][new_x] == 1 and is_crashed == 0:
                res[new_y][new_x][is_crashed + 1] = res[y][x][is_crashed] + 1
                q.append([new_y, new_x, is_crashed + 1])
                print(res)
                print()

print(res)

ans = max(res[c - 1][r - 1][0], res[c - 1][r - 1][1])
if ans == 0:
    print(-1)
else:
    print(ans)
