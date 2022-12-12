import sys

stack = list()


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0


def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]


n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        push(order[1])
    elif order[0] == "pop":
        print(pop())
    elif order[0] == "size":
        print(size())
    elif order[0] == "empty":
        print(empty())
    elif order[0] == "top":
        print(top())





