import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))
res = [0]


def find_place(x):
    s = 0
    e = len(res) - 1
    while s <= e:
        mid = (s + e) // 2
        if res[mid] == x:
            return mid
        elif res[mid] < x:
            s = mid + 1
        else:
            e = mid - 1

    return s


for i in range(len(data)):
    if data[i] > res[-1]:
        res.append(data[i])
    else:
        res[find_place(data[i])] = data[i]

print(len(res) - 1)
