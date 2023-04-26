import sys
sys.setrecursionlimit(10 ** 6)


def solution(n, results):
    w_l = [[0, 0] for _ in range(n + 1)]
    res = 0

    def dfs(head, start, w_l):

        for r in results:
            s = r[0]
            e = r[1]
            if s == start and visited[e] == 0:
                w_l[head][0] += 1
                w_l[e][1] += 1
                visited[e] = 1
                dfs(head, e, w_l)

    for i in range(1, n + 1):
        visited = [0 for _ in range(n + 1)]
        dfs(i, i, w_l)

    for d in w_l:
        if sum(d) == n - 1:
            res += 1

    return res


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
