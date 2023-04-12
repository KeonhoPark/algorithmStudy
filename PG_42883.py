def solution(number, k):
    number = list(number)
    length = len(number) - k
    res = ''
    idx = 0
    while len(res) < length:
        tmp = number[idx:len(number) - (length - len(res)) + 1]

        mx = '0'
        mx_idx = 0
        for i in range(len(tmp)):
            if tmp[i] == '9':
                mx = tmp[i]
                mx_idx = i
                break
            if tmp[i] > mx:
                mx = tmp[i]
                mx_idx = i

        res += mx
        idx += (mx_idx + 1)

    return res


print(solution("4177252841", 4))
