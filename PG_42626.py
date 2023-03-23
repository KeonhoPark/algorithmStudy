import heapq


def solution(sco, k):
    count = 0
    flag = 0
    heapq.heapify(sco)

    while sco:
        first = heapq.heappop(sco)

        if first >= k:
            flag = 1
            break

        elif sco and first < k:
            second = heapq.heappop(sco)
            heapq.heappush(sco, first + (second * 2))
            count += 1

    if flag == 0:
        return -1
    else:
        return count


print(solution([1, 1, 1, 1, 2, 2], 100))
