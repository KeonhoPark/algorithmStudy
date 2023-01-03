from collections import deque

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0
l = 0
q = deque()
m = n // 2
count += apple[m][m]
visited[m][m] = 1
q.append([m, m])

while True:
    if l == m:
        break

    for i in range(len(q)):
        c = q.popleft()
        for j in range(4):
            x = c[0] + dx[j]
            y = c[1] + dy[j]
            if visited[x][y] == 0:
                count += apple[x][y]
                visited[x][y] = 1
                q.append([x, y])

    l += 1

print(count)
