import sys
sys.setrecursionlimit(10 ** 6)

n, e, s = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(n + 1)]
res = [0 for _ in range(n + 1)]
rank = 1

for i in range(e):
    start, end = map(int, sys.stdin.readline().split())
    edge[start].append(end)
    edge[end].append(start)

for e in edge:
    e.sort(reverse=True)


def dfs(s):
    global rank
    res[s] = rank
    rank += 1
    for e in edge[s]:
        if res[e] == 0:
            dfs(e)


dfs(s)
for i in range(1, len(res)):
    print(res[i])
