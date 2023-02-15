n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]
res = [0 for _ in range(m)]
flag = [0 for _ in range(n + 1)]


def dfs(l):
    if l == m:
        print(*res)
        return

    else:
        for i in range(len(data)):
            if flag[i] == 0:
                res[l] = data[i]
                flag[i] = 1
                dfs(l + 1)
                flag[i] = 0


dfs(0)




