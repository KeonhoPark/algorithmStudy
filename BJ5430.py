import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    order = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(sep=','))
    j = 0
    k = len(q) - 1
    if n == 0:
        q = []
    r_count = 0
    for o in order:
        if o == 'D':
            if len(q) == 0:
                print("error")
                break
            elif r_count % 2 == 1:
                q.pop()
            elif r_count % 2 == 0:
                q.popleft()
        else:
            r_count += 1
    else:
        if r_count % 2 == 0:
            print('[', end='')
            print(*q, sep=',', end='')
            print(']')
        else:
            q.reverse()
            print('[', end='')
            print(*q, sep=',', end='')
            print(']')
