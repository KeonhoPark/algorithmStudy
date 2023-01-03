import copy
from collections import deque

n = int(input())
apple = [[0]] * n
for i in range(n):
    apple[i] = list(map(int, input().split()))

q = list()
q = deque(q)
c_q = list()
c_q = deque(c_q)
visited = [[0 for i in range(n)] for j in range(n)]
m = n // 2
l = 0
count = 0

q.append([m, m])
while l < m + 1:
    c = q.popleft()
    x = c[0]
    y = c[1]
    visited[x][y] = 1
    count += apple[x][y]

    if l != m:
        if visited[x - 1][y] == 0:
            c_q.append([x - 1, y])
            visited[x - 1][y] = 1
        if visited[x + 1][y] == 0:
            c_q.append([x + 1, y])
            visited[x + 1][y] = 1
        if visited[x][y - 1] == 0:
            c_q.append([x, y - 1])
            visited[x][y - 1] = 1
        if visited[x][y + 1] == 0:
            c_q.append([x, y + 1])
            visited[x][y + 1] = 1

    if len(q) == 0:
        l += 1
        q = copy.deepcopy(c_q)
        c_q.clear()

print(count)
