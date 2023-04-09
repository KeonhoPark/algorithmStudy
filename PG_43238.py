def solution(n, times):
    times.sort()
    shortest = times[0]

    start = shortest
    end = shortest * n
    min_time = end

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for t in times:
            count += (mid // t)
            if count >= n:
                end = mid - 1
                min_time = mid
                break

        else:
            if count < n:
                start = mid + 1

    return min_time


solution(6, [7, 10])
