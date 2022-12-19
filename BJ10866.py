from collections import deque
import sys

n = int(sys.stdin.readline())
data = list()
data = deque(data)


def push_front(x):
    data.appendleft(x)


def push_back(x):
    data.append(x)


def pop_front():
    if len(data) == 0:
        return -1
    else:
        return data.popleft()


def pop_back():
    if len(data) == 0:
        return -1
    else:
        return data.pop()


def size():
    return len(data)


def empty():
    if len(data) == 0:
        return 1
    else:
        return 0


def front():
    if len(data) == 0:
        return -1
    else:
        return data[0]


def back():
    if len(data) == 0:
        return -1
    else:
        return data[-1]


for i in range(n):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push_front':
        push_front(int(order[1]))
    elif order[0] == 'push_back':
        push_back(int(order[1]))
    elif order[0] == 'pop_front':
        print(pop_front())
    elif order[0] == 'pop_back':
        print(pop_back())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())
