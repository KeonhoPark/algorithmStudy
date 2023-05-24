def solution(a, b):
    mn = min(a, b)
    max_devide = 1
    for i in range(2, mn + 1):
        if a % i == 0 and b % i == 0 and i > max_devide:
            max_devide = i

    a //= max_devide
    b //= max_devide
    if b == 1:
        return 1

    if b % 2 == 0 or b % 5 == 0:
        for i in range(2, b):
            if i == 2 or i == 5:
                continue
            if not (i % 2 == 0 or i % 5 == 0) and b % i == 0:
                return 2
        return 1

    else:
        return 2
