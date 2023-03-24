def solution(numbers):
    numbers = list(map(str, numbers))
    tmp = list()
    res = ''

    for n in numbers:
        tmp.append(((n * 4)[:4:], len(n)))

    tmp.sort(reverse=True)

    for t in tmp:
        res += t[0][:t[1]:]

    if int(res) == 0:
        return "0"
    else:
        return res
