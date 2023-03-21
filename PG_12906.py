from collections import deque


def solution(arr):
    q = deque()
    q.append(arr[0])

    for a in arr:
        if a != q[-1]:
            q.append(a)

    # print(q)
    return list(q)
