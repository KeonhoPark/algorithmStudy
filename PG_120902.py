def solution(my_string):
    my_string = list(my_string.split(' '))
    res = int(my_string[0])

    for i in range(1, len(my_string) - 1):
        if my_string[i] == '+':
            res += int(my_string[i + 1])
        elif my_string[i] == '-':
            res -= int(my_string[i + 1])

    return res
