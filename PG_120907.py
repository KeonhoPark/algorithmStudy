def solution(quiz):
    answer = []

    for q in quiz:
        tmp = q.split(' ')
        tmp.remove('=')
        print(tmp)
        res = 0
        if tmp[1] == '+':
            res = int(tmp[0]) + int(tmp[2])
        elif tmp[1] == '-':
            res = int(tmp[0]) - int(tmp[2])

        if res == int(tmp[3]):
            answer.append('O')
        else:
            answer.append('X')

    return answer
