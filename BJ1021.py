from collections import deque

n, m = map(int, input().split())

data = list(map(int, input().split()))
q = list(i for i in range(1, n+1))
q = deque(q)


def left():
    q.append(q.popleft())


def right():
    q.appendleft(q.pop())


count = 0
for d in data:
    while True:
        if d == q[0]:
            q.popleft()
            break
        elif q.index(d) > (len(q)-1) // 2:
            while d != q[0]:
                right()
                count += 1
        elif q.index(d) <= (len(q)-1) // 2:
            while d != q[0]:
                left()
                count += 1

print(count)


