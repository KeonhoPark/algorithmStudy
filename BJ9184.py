import sys

data = [[[0 for _ in range(-50, 51)] for _ in range(-50, 51)] for _ in range(-50, 51)]


def dfs(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif data[a][b][c] != 0:
        return data[a][b][c]
    elif a > 20 or b > 20 or c > 20:
        data[20][20][20] = dfs(20, 20, 20)
        return data[20][20][20]
    elif a < b < c:
        data[a][b][c-1] = dfs(a, b, c - 1)
        data[a][b-1][c-1] = dfs(a, b - 1, c - 1)
        data[a][b-1][c] = dfs(a, b - 1, c)
        return data[a][b][c-1] + data[a][b-1][c-1] - data[a][b-1][c]
    else:
        data[a-1][b][c] = dfs(a - 1, b, c)
        data[a-1][b-1][c] = dfs(a - 1, b - 1, c)
        data[a-1][b][c-1] = dfs(a - 1, b, c - 1)
        data[a-1][b-1][c-1] = dfs(a - 1, b - 1, c - 1)
        return data[a-1][b][c] + data[a-1][b-1][c] + data[a-1][b][c-1] - data[a-1][b-1][c-1]


a = b = c = 0
while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({0}, {1}, {2}) =".format(a, b, c), dfs(a, b, c))
