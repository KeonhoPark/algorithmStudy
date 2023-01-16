from collections import deque

n, m = map(int, input().split())

data = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1

degree = [0 for _ in range(n+1)]
q = deque()

for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] == 1:
            degree[j] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while True:
    p = q.popleft()
    print(p, end=" ")
    for i in range(1, n+1):
        if data[p][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)

    if len(q) == 0:
        break

print(degree)
