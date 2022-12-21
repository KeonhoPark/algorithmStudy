from collections import deque

n = int(input())
res = deque(list())


def bi(x):
    if x == 1:
        res.appendleft(1)
    else:
        res.appendleft(x % 2)
        bi(x // 2)


bi(n)
for r in res:
    print(r, end='')

