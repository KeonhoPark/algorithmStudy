from collections import deque


def solution(queue1, queue2):
    def oper(s1, s2):
        if s1 > s2:
            n = queue1.popleft()
            queue2.append(n)
            return s1 - n, s2 + n
        elif s1 < s2:
            n = queue2.popleft()
            queue1.append(n)
            return s1 + n, s2 - n

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    length = len(queue1)
    s1 = sum(queue1)
    s2 = sum(queue2)
    # MAX = max(max(queue1), max(queue2))
    if (s1 + s2) % 2 == 1:
        return -1
    else:
        count = 0

        while True:
            if s1 == s2:
                return count
            elif length * 4 <= count:
                return -1
            else:
                new_s1, new_s2 = oper(s1, s2)
                # print(queue1, queue2, new_dif)
                s1 = new_s1
                s2 = new_s2
                count += 1
