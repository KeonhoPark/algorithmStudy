from collections import deque

n, k = map(int, input().split())
q = [i for i in range(1, n+1)]
q = deque(q)
res = list()

while len(q) != 0:
    count = 1
    while count < k:
        q.append(q.popleft())
        count += 1
    res.append(q.popleft())

print('<', end="")
print(*res, sep=', ', end="")
print('>', end="")















