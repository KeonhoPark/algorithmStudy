def solution(my_str, n):
    res = list()
    i = 0
    while i < len(my_str):
        res.append(my_str[i:i + n])
        i += n

    return res
