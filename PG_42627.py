import heapq


def solution(jobs):
    total = 0
    n = len(jobs)
    idx = 0
    cur_time = 0
    prior = -1
    heap = []

    while idx < n:
        for job in jobs:
            start = job[0]
            duration = job[1]
            if prior < start <= cur_time:
                heapq.heappush(heap, [duration, start])

        if heap:
            duration, start = heapq.heappop(heap)
            prior = cur_time
            total += (cur_time - start + duration)
            cur_time += duration
            idx += 1

        else:
            cur_time += 1

    print(total // n)
    return total // n


solution([[0, 3], [1, 9], [2, 6]])
