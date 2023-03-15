import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
MAX = sys.maxsize

graph = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]
res = [[[i] for _ in range(n + 1)] for i in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0
    res[i][i] = 0

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    if c < graph[s][e]:
        graph[s][e] = c


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                res[i][j] = res[i][k] + res[k][j]

for i in range(1, len(graph)):
    for j in range(1, len(graph)):
        if graph[i][j] == MAX:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1, len(res)):
    for j in range(1, len(res)):
        if graph[i][j] != MAX and res[i][j] != 0:
            res[i][j].append(j)
            print(len(res[i][j]), *res[i][j])

        else:
            print(0)
