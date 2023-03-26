n, m = map(int, input().split())
res = [0 for _ in range(m)]


def dfs(l, s):
    if l == m:
        print(*res)
        return
    else:
        for i in range(s, n + 1):
            res[l] = i
            dfs(l + 1, i)


dfs(0, 1)
