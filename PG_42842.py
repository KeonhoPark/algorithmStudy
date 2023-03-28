def solution(brown, yellow):
    res = list()

    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            bound = (h * 2) + (w * 2) + 4
            if bound == brown:
                return [w + 2, h + 2]
