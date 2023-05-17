def solution(survey, choices):
    jipyo = [[[0, 'R'], [0, 'T']], [[0, 'C'], [0, 'F']], [[0, 'J'], [0, 'M']], [[0, 'A'], [0, 'N']]]
    res = ''

    def find_index(type):
        for m in range(len(jipyo)):
            for n in range(len(jipyo[m])):
                if type == jipyo[m][n][1]:
                    return m, n

    def calc_jipyo():
        for i in range(len(survey)):
            tmp = list(survey[i])
            first = tmp[0]
            second = tmp[1]

            if choices[i] == 1:
                m, n = find_index(first)
                jipyo[m][n][0] += 3

            elif choices[i] == 2:
                m, n = find_index(first)
                jipyo[m][n][0] += 2

            elif choices[i] == 3:
                m, n = find_index(first)
                jipyo[m][n][0] += 1

            elif choices[i] == 5:
                m, n = find_index(second)
                jipyo[m][n][0] += 1

            elif choices[i] == 6:
                m, n = find_index(second)
                jipyo[m][n][0] += 2

            elif choices[i] == 7:
                m, n = find_index(second)
                jipyo[m][n][0] += 3

    calc_jipyo()

    for i in range(len(jipyo)):
        jipyo[i].sort(reverse=True)
        if jipyo[i][0][0] == jipyo[i][1][0]:
            res += jipyo[i][1][1]
        else:
            res += jipyo[i][0][1]

    return res
