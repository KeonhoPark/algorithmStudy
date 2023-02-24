import sys
from collections import deque

l, s = map(int, sys.stdin.readline().split())
data = [i for i in range(101)]
visited = [0 for i in range(101)]
res = [1e9 for i in range(101)]
for _ in range(l + s):
    start, end = map(int, sys.stdin.readline().split())
    data[start] = end

q = deque()
q.append(1)
visited[1] = 1
res[1] = 0

while q:
    p = q.popleft()
    cur = data[p]

    if cur == 100:
        break
    for i in range(cur + 1, cur + 7):
        if 1 <= i <= 100 and visited[i] == 0:
            q.append(data[i])
            visited[i] = 1
            res[data[i]] = min(res[cur] + 1, res[data[i]])

print(res[100])
