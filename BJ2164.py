from collections import deque

n = int(input())
q = list()
q = deque(q)

for i in range(1, n + 1):
    q.append(i)


def throw():
    q.popleft()


def trans():
    pop_card = q.popleft()
    q.append(pop_card)


if n == 1:
    print(1)
else:
    while len(q) > 1:
        throw()
        trans()

    print(q[-1])




