def solution(s):
    res = 0
    s = list(s.split(' '))
    while s:
        if s[-1] == 'Z':
            s.pop()
            s.pop()
        else:
            res += int(s[-1])
            s.pop()

    return res

solution("1 2 Z 3")