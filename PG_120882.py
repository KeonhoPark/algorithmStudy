def solution(score):
    average = []
    rank = []
    tmp = []

    for i in range(len(score)):
        average.append(sum(score[i]) / 2)

    tmp = sorted(average, reverse=True)

    for a in average:
        for i in range(len(tmp)):
            if a == tmp[i]:
                rank.append(i + 1)
                break

    return rank
