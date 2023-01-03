from collections import deque

data = [list(map(int, input().split())) for _ in range(7)]
visited = [[0 for _ in range(7)] for _ in range(7)]
# min_count = 1e9
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
visited[0][0] = 1
q.append([0, 0])
count = 0

while True:
    flag = 0

    for i in range(len(q)):
        c = q.popleft()
        if c[0] == 6 and c[1] == 6:
            flag = 1
            break
        for j in range(4):
            x = c[0] + dx[j]
            y = c[1] + dy[j]
            if 0 <= x <= 6 and 0 <= y <= 6:
                if visited[x][y] == 0 and data[x][y] == 0:
                    visited[x][y] = 1
                    q.append([x, y])

    count += 1

    if flag == 1:
        print(count - 1)
        break
    elif len(q) == 0:
        print(-1)
        break

