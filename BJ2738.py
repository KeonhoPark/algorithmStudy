n, m = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(m)] for j in range(n)]
ans = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    b[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        ans[i][j] = a[i][j] + b[i][j]

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()




