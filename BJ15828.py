import sys
from collections import deque

n = int(sys.stdin.readline())
q = list()
q = deque(q)
m = int(sys.stdin.readline())
while m != -1:
    if m == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(m)

    m = int(sys.stdin.readline())

if len(q) == 0:
    print('empty')
else:
    for x in q:
        print(x, end=" ")


