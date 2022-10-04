n = int(input())
data = []


def func(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return func(a - 1) + func(a - 2) + func(a - 3)


for i in range(n):
    data.append(int(input()))

for j in range(n):
    print(func(data[j]))


