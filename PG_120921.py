from collections import deque


def solution(A, B):
    count = 0

    if A == B:
        return 0
    else:
        A = deque(A)
        B = deque(B)
        for _ in range(len(A)):
            A.appendleft(A.pop())
            count += 1
            if A == B:
                return count

        return -1
