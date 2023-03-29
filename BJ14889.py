import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
flag = [0 for _ in range(n)]
start = list()
res = 1e9


def dfs(l, s):
    global res

    if l == n // 2:
        s_score = 0
        l_score = 0
        link = list()
        for i in range(n):
            if i not in start:
                link.append(i)

        for i in start:
            for j in start:
                s_score += data[i][j]

        for i in link:
            for j in link:
                l_score += data[i][j]

        res = min(res, abs(s_score - l_score))
        return
    else:
        for i in range(s, n):
            if flag[i] == 0:
                flag[i] = 1
                start.append(i)
                dfs(l + 1, i)
                flag[i] = 0
                start.pop()


dfs(0, 0)
print(res)
