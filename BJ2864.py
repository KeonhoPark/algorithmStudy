a, b = map(int, input().split())


def to_max(n):
    res = n
    i = 0
    while n > 0:
        if n % 10 == 5:
            res += 10 ** i
        i += 1
        n = n // 10

    return res


def to_min(n):
    res = n
    i = 0
    while n > 0:
        if n % 10 == 6:
            res -= 10 ** i
        i += 1
        n = n // 10

    return res


print(to_min(a) + to_min(b), to_max(a) + to_max(b), sep=" ")

# a, b = input().split()
# min = int(a.replace('6', '5')) + int(b.replace('6', '5'))
# max = int(a.replace('5', '6')) + int(b.replace('5', '6'))
# print(min, max, sep=" ")



