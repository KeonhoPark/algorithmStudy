def solution(sizes):
    sizes.sort(reverse=True)

    w = list()
    h = list()
    for s in sizes:
        w.append(s[0])
        h.append(s[1])

    min_w = max(w) * max(h)

    for i in range(len(sizes)):
        w[i], h[i] = h[i], w[i]
        max_w = max(w)
        max_h = max(h)
        tmp = max_w * max_h
        if tmp < min_w:
            min_w = tmp

    return (min_w)