n = int(input())
m = int(input())

dis = [[100001 for i in range(n)] for j in range(n)]
for i in range(n):
    dis[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if dis[a-1][b-1] > c:
        dis[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j])

for i in range(n):
    for j in range(n):
        if dis[i][j] == 100001:
            print(0, end=" ")
        else:
            print(dis[i][j], end=" ")
    print()

