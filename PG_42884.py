def solution(routes):
    routes.sort(key=lambda x: x[1])
    res = 0
    cur_pos = -30001

    for start, end in routes:
        if cur_pos < start:
            res += 1
            cur_pos = end

    return res
