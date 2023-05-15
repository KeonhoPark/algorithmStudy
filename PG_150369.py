def get_max_idx(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] != 0:
            return i

    return 0


def work(lst, max_idx, cap):
    for _ in range(cap):
        lst[max_idx] -= 1

        while lst[max_idx] == 0:
            if max_idx == 0:
                return max_idx - 1
            else:
                max_idx -= 1

    return max_idx


def solution(cap, n, deliveries, pickups):
    total = 0
    d_idx = get_max_idx(deliveries)
    p_idx = get_max_idx(pickups)

    if d_idx == 0 and p_idx == 0:
        return 0

    while d_idx >= 0 or p_idx >= 0:
        total += (max(d_idx + 1, p_idx + 1) * 2)

        d_idx = work(deliveries, d_idx, cap)
        p_idx = work(pickups, p_idx, cap)

    return total
