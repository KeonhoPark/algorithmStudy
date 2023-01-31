n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(m)]

res = [[0 for _ in range(k)] for _ in range(n)]

for j in range(k):
    for a in range(n):
        tmp = 0
        for b in range(m):
            tmp += matrix1[a][b] * matrix2[b][j]
        res[a][j] = tmp

for i in range(n):
    print(*res[i], sep=' ')


