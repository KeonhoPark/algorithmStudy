n, m = map(int, input().split())
res = [0 for _ in range(m)]


def dfs(l):
    if l == m:
        print(*res)
        return
    else:
        for i in range(1, n + 1):
            res[l] = i
            dfs(l + 1)


dfs(0)
