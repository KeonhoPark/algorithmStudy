import sys

sys.setrecursionlimit(10 ** 6)


def solution(m, n, puddles):
    end = [m, n]
    graph = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for p in puddles:
        graph[p[1]][p[0]] = -1

    dx = [0, 1]
    dy = [1, 0]

    def dfs(x, y):
        if x == end[0] and y == end[1]:
            return 1

        if graph[y][x] != 0:
            return graph[y][x]

        else:
            for i in range(2):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if 1 <= new_x <= m and 1 <= new_y <= n and graph[new_y][new_x] != -1:
                    graph[y][x] += dfs(new_x, new_y)

            return graph[y][x]

    dfs(1, 1)
    print(graph)
    return graph[1][1] % 1000000007
