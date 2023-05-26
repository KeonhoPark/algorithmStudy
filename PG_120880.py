def solution(numlist, n):
    #     dist_num = []
    #     res = []

    #     for num in numlist:
    #         dist_num.append([abs(num - n), n - num, num])

    #     dist_num.sort()

    #     for x in dist_num:
    #         res.append(x[2])

    res = sorted(numlist, key=lambda x: [abs(x - n), n - x])

    return res
