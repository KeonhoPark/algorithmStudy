from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
pdx = [0, -1]
pdy = [-1, 0]
q = deque()
visited = [[0 for _ in range(n)] for _ in range(n)]

q.append([0, 0])
visited[0][0] = 1

while True:

    c = q.popleft()
    x = c[0]
    y = c[1]

    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        m = 1e9
        if 0 <= new_x < n and 0 <= new_y < n and visited[new_y][new_x] == 0:
            q.append([new_x, new_y])
            visited[new_y][new_x] = 1
            for j in range(2):
                p_x = new_x + pdx[j]
                p_y = new_y + pdy[j]
                if 0 <= p_x < n and 0 <= p_y < n and data[p_y][p_x] < m:
                    m = data[p_y][p_x]

            data[new_y][new_x] += m

    if len(q) == 0:
        break

print(data[n - 1][n - 1])
