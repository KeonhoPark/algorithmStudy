import sys
sys.setrecursionlimit(10 ** 6)


def dfs(s, count, graph, visited):
    for i in range(1, len(graph)):
        if visited[i] == 0 and graph[s][i] == 1:
            # print(s, i)
            visited[i] = 1
            dfs(i, count + 1, graph, visited)


def solution(n, wires):
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    mn = 1e9

    for i in range(n + 1):
        graph[i][i] = 1

    for w in wires:
        graph[w[0]][w[1]] = 1
        graph[w[1]][w[0]] = 1

    for w in wires:
        visited = [0 for _ in range(n + 1)]
        visited[1] = 1
        graph[w[0]][w[1]] = 0
        graph[w[1]][w[0]] = 0

        dfs(1, 1, graph, visited)
        tmp = abs(sum(visited) - (n - (sum(visited))))
        if tmp < mn:
            mn = tmp

        graph[w[0]][w[1]] = 1
        graph[w[1]][w[0]] = 1

    return mn
