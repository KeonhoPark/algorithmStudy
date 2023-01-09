n = int(input())
data = [0] * (n + 1)


def dfs(s):
    if s == 1 or s == 2:
        return s
    if data[s] != 0:
        return data[s]
    else:
        data[s] = dfs(s - 1) + dfs(s - 2)
        return data[s]


print(dfs(n))
