from collections import deque

m, n = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque()
dis = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append((i, j))

while q:
    tmp = q.popleft()
    for i in range(4):
        xx = tmp[0]+dx[i]
        yy = tmp[1]+dy[i]
        if 0 <= xx < n and 0 <= yy < m and matrix[xx][yy] == 0:
            matrix[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            q.append((xx, yy))

flag = 1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(n):
        for j in range(m):
          if dis[i][j] > result:
              result = dis[i][j]
    print(result)

else:
    print(-1)








