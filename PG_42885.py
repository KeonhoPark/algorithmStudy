from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    count = 0

    while people:
        mn = people.popleft()
        count += 1

        while people:
            mx = people.pop()
            if mn + mx <= limit:
                break
            else:
                count += 1

        if not people:
            break

    return count


solution([2, 3, 7, 7, 10], 10)
