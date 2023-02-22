import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
visited[1] = 1
q = deque()
q.append(1)
count = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    data[s][e] = 1
    data[e][s] = 1

while q:
    s = q.popleft()
    for i in range(1, n + 1):
        if data[s][i] == 1 and visited[i] == 0:
            q.append(i)
            visited[i] = 1
            count += 1

print(count)






