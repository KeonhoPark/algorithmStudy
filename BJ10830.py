n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


def dfs(b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    else:
        tmp = dfs(b // 2)
        new_tmp = mul(tmp, tmp)
        if b % 2 == 0:
            return new_tmp
        else:
            return mul(new_tmp, matrix)


def mul(matrix1, matrix2):
    res = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for a in range(n):
            tmp = 0
            for b in range(n):
                tmp += matrix1[a][b] * matrix2[b][j]
            res[a][j] = tmp % 1000

    return res


res = dfs(b)
for i in range(n):
    print(*res[i])



