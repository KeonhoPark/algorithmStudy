def solution(prices):
    res = list()

    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                count += 1
                break
            else:
                count += 1
        res.append(count)

    res.append(0)
    return res
