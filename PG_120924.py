def solution(common):
    s1 = common[2] - common[1]
    s2 = common[1] - common[0]
    d1 = 0
    d2 = 0

    if common[1] != 0 and common[0] != 0:
        d1 = common[2] / common[1]
        d2 = common[1] / common[0]

    if s1 == s2:
        return common[-1] + s1
    elif d1 == d2:
        return common[-1] * d1
    