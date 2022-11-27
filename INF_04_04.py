n, c = map(int, input().split())
data = list()
for i in range(n):
    data.append(int(input()))

data.sort()


def cnt(dis):
    count = 1
    start = data[0]
    for i in range(1, n):
        if data[i] - start >= dis:
            count += 1
            start = data[i]

    return count


l = 1
r = data[n-1]
while l <= r:
    m = (l+r) // 2
    if cnt(m) >= c:
        res = m
        l = m + 1
    else:
        r = m - 1

print(res)








