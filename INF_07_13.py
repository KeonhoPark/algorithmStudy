from collections import deque

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]
count = 0


def cluster(x, y):
    global count
    q = deque()
    q.append([x, y])

    while True:
        c = q.popleft()
        x = c[0]
        y = c[1]
        island[x][y] = 0
        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if island[new_x][new_y] == 1:
                    q.append([new_x, new_y])

        if len(q) == 0:
            count += 1
            break


for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            cluster(i, j)


print(count)




