def solution(answers):
    score = [0 for _ in range(3)]
    res = list()

    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1251
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    for i in range(len(answers)):
        if answers[i] == s1[i]:
            score[0] += 1
        if answers[i] == s2[i]:
            score[1] += 1
        if answers[i] == s3[i]:
            score[2] += 1

    m = max(score)
    for i in range(len(score)):
        if score[i] == m:
            res.append(i + 1)

    return res