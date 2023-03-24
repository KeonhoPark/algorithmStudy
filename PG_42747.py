def solution(citations):
    citations.sort(reverse=True)
    h_list = list()

    max_h = -1
    for i in range(10001):
        count = 0
        for c in citations:
            if c >= i:
                count += 1
            else:
                break

        if count >= i and count > max_h:
            h_list.append(i)

    return max(h_list)
