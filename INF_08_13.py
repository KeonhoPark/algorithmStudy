n, m = map(int, input().split())
M = 1e9
dis = [[M for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i] = 0

for _ in range(m):
    i, j, c = map(int, input().split())
    dis[i][j] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == M:
            dis[i][j] = 'M'
        print(dis[i][j], end=' ')
    print()


