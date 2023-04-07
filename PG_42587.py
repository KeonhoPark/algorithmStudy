from collections import deque


def solution(priorities, location):
    q = deque()
    res = dict()

    for i in range(len(priorities)):
        q.append((priorities[i], i))

    rank = 1
    while q:
        cur_doc = q.popleft()
        for doc in q:
            if doc[0] > cur_doc[0]:
                q.append(cur_doc)
                break

        else:
            res[cur_doc[1]] = rank
            rank += 1

    return res[location]
