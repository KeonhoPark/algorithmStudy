from collections import deque

n = int(input())
house = [list(map(int, input())) for _ in range(n)]
danji = 0
count = list()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def cluster(x, y):
    global danji
    cnt = 1
    q = deque()
    house[x][y] = 0
    q.append([x, y])
    while True:
        c = q.popleft()
        x = c[0]
        y = c[1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if house[new_x][new_y] == 1:
                    cnt += 1
                    house[new_x][new_y] = 0
                    q.append([new_x, new_y])
        if len(q) == 0:
            count.append(cnt)
            danji += 1
            return


for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            cluster(i, j)

print(danji)
count.sort()
print(*count, sep="\n")

