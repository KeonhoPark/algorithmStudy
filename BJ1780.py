n = int(input())
data = [0 for _ in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))

c1 = c2 = c3 = 0


def dfs(y, x, n):
    c = check(y, x, n)

    if c == 1 or c == 2 or c == 3:
        return

    else:
        new_n = n // 3
        for i in range(y, y + n, new_n):
            for j in range(x, x + n, new_n):
                dfs(i, j, new_n)


def check(y, x, n):
    global c1, c2, c3
    s = data[y][x]
    for i in range(y, y + n):
        for j in range(x, x + n):
            if s != data[i][j]:
                return -1

    if s == -1:
        c1 += 1
        return 1
    elif s == 0:
        c2 += 1
        return 2
    elif s == 1:
        c3 += 1
        return 3


dfs(0, 0, n)
print(c1)
print(c2)
print(c3)
