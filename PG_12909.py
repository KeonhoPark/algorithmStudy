from collections import deque


def solution(s):
    q = deque()
    for x in s:
        if x == '(':
            q.append(x)
        elif q and x == ')':
            q.popleft()
        else:
            return False

    print(q)
    if q:
        return False
    else:
        return True
    