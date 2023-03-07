import sys


def fw():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                data[i][j] = min(data[i][j], data[i][k] + data[k][j])


n, e = map(int, sys.stdin.readline().split())
data = [[int(1e9) for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    data[a][b] = w

fw()

ans = 1e9
for i in range(1, n + 1):
    ans = min(ans, data[i][i])

if ans == 1e9:
    print(-1)
else:
    print(ans)
