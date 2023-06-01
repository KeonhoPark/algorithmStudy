def solution(lines):
    count = 0
    graph = [0 for _ in range(201)]
    starts = [l[0] for l in lines]
    mn = min(starts)

    for l in lines:
        if mn < 0:
            l[0] -= mn
            l[1] -= mn
        for i in range(l[0] + 1, l[1] + 1):
            graph[i] += 1

    for g in graph:
        if g > 1:
            count += 1

    return count
