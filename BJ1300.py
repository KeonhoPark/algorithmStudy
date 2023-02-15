n = int(input())
k = int(input())

s = 1
e = k
res = 0

while s <= e:
    mid = (s + e) // 2
    tmp = 0
    for i in range(1, n + 1):
        tmp += min(mid // i, n)

    if tmp >= k:
        res = mid
        e = mid - 1

    else:
        s = mid + 1

print(res)


