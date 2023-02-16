n, m = map(int, input().split())
flag = [0 for i in range(n + 1)]
res = [0 for _ in range(m)]


def dfs(l, s):
    if l == m:
        print(*res)
        return

    else:
        for i in range(s, n + 1):
            if flag[i] == 0:
                res[l] = i
                flag[i] = 1
                dfs(l + 1, i)
                flag[i] = 0


dfs(0, 1)
