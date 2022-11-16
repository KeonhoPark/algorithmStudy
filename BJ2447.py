n = int(input())


def pattern_3(n):
    if n == 1:
        return ['*']

    stars = pattern_3(n // 3)
    l = []

    for star in stars:
        l.append(star * 3)
    for star in stars:
        l.append(star + ' '*(n//3) + star)
    for star in stars:
        l.append(star * 3)

    return l

list = pattern_3(n)
for i in range(len(list)):
    print(list[i])
