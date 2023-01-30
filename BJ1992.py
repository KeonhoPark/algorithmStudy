n = int(input())
data = [0 for _ in range(n)]

for i in range(n):
    data[i] = list(map(int, input()))

res = list()


def dfs(y, x, n):
    c = check(y, x, n)
    if n == 1:
        res.append(data[y][x])
    elif c != 2:
        res.append(c)
    else:
        if c == 2:
            new_n = n // 2
            res.append('(')
            dfs(y, x, new_n)
            dfs(y, x + new_n, new_n)
            dfs(y + new_n, x, new_n)
            dfs(y + new_n, x + new_n, new_n)
            res.append(')')
        else:
            res.append(c)


def check(y, x, n):
    s = 0
    for i in range(y, y + n):
        s += sum(data[i][x:x + n])

    if s == 0:
        return 0
    elif s == n ** 2:
        return 1
    else:
        return 2


dfs(0, 0, n)
print(*res, sep="")
