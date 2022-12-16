import sys
from collections import deque

q = list()
q = deque(q)
n = int(input())


def push(x):
    q.append(x)


def pop():
    if empty() == 1:
        return -1
    else:
        return q.popleft()


def size():
    return len(q)


def empty():
    if len(q) == 0:
        return 1
    else:
        return 0


def front():
    if empty() == 1:
        return -1
    else:
        return q[0]


def back():
    if empty() == 1:
        return -1
    else:
        return q[-1]


for i in range(n):
    o = list(sys.stdin.readline().split())
    if o[0] == 'push':
        push(o[1])
    elif o[0] == 'pop':
        print(pop())
    elif o[0] == 'size':
        print(size())
    elif o[0] == 'empty':
        print(empty())
    elif o[0] == 'front':
        print(front())
    elif o[0] == 'back':
        print(back())
