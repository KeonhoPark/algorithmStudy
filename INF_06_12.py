n, e = map(int, input().split())
matrix = [[0 for i in range(n)] for j in range(n)]

for k in range(e):
    s, e, w = map(int, input().split())
    matrix[s-1][e-1] = w


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


