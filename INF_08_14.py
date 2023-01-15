n = int(input())
M = 1e9
dis = [[M for _ in range(n+1)] for _ in range(n+1)]
a, b = 0, 0
score = 1e9
res = list()

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b] = dis[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, len(dis)):
    m = max(dis[i][1:])
    if m < score:
        score = m

for i in range(1, len(dis)):
    if max(dis[i][1:]) == score:
        res.append(i)

print(score, len(res), sep=' ')
print(*res, end=' ')



