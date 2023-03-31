

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    i = 0
    while i < len(reserve):
        if reserve[i] in lost:
            lost.remove(reserve[i])
            reserve.remove(reserve[i])

        else:
            i += 1

    i = 0
    while i < len(reserve):
        if len(lost) == 0:
            break

        elif reserve[i] - 1 in lost:
            lost.remove(reserve[i] - 1)
            reserve.remove(reserve[i])

        elif reserve[i] + 1 in lost:
            lost.remove(reserve[i] + 1)
            reserve.remove(reserve[i])

        else:
            i += 1

    return n - len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
