def solution(num, total):
    res = list()

    mid = total // num
    if num % 2 == 1:
        for i in range(mid - (num // 2), mid + (num // 2) + 1):
            res.append(i)

    else:
        for i in range(mid - (num // 2) + 1, mid + (num // 2) + 1):
            res.append(i)

    return res
