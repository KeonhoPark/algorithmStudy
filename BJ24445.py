import sys
from collections import deque

n, e, s = map(int, sys.stdin.readline().split())
edge = [[] for _ in range(n + 1)]
q = deque()
q.append(s)
res = [0 for _ in range(n + 1)]
res[s] = 1
rank = 2

for i in range(e):
    start, end = map(int, sys.stdin.readline().split())
    edge[start].append(end)
    edge[end].append(start)

for e in edge:
    e.sort(reverse=True)

while q:
    s = q.popleft()
    for e in edge[s]:
        if res[e] == 0:
            q.append(e)
            res[e] = rank
            rank += 1

for i in range(1, len(res)):
    print(res[i])
