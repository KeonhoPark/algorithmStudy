import sys

n = int(sys.stdin.readline())
data1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

data1.sort()

# print(data1)
# print(data2)

mn = data1[0]
mx = data1[-1]


def find(data1, d2, l, r):
    mid = (l + r) // 2
    if d2 == data1[mid]:
        return 1
    elif l >= r:
        return 0
    elif d2 > data1[mid]:
        return find(data1, d2, mid + 1, r)
    else:
        return find(data1, d2, l, mid - 1)


for d2 in data2:
    if d2 < mn or d2 > mx:
        print(0)
    else:
        print(find(data1, d2, 0, len(data1)-1))
