import sys

n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
house.sort()
res = [0 for _ in range(n)]

if n == 1 or n == 2:
    print(house[0])

else:
    mid = (n // 2) - 1
    m = 0
    res = mid
    for i in range(n):
        m += abs(house[mid] - house[i])

    for i in range(mid + 1, n):
        tmp = 0
        for j in range(n):
            tmp += abs(house[i] - house[j])

        if m <= tmp:
            break
        else:
            m = tmp
            res = i

    for i in range(mid - 1, 0, -1):
        tmp = 0
        for j in range(n):
            tmp += abs(house[i] - house[j])

        if m <= tmp:
            break
        else:
            m = tmp
            res = i

    print(house[res])




