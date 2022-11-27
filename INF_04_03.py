n, m = map(int, input().split())
data = list(map(int, input().split()))

l = 1
r = sum(data)
count = 0
res = list()

while l <= r:
    mid = (l+r) // 2
    count = 0
    sum = 0
    for i in range(len(data)):
        sum += data[i]
        if i == len(data) - 1:
            count += 1
            break
        elif sum+data[i+1] > mid:
            sum = 0
            count += 1

    if count == m:
        res = mid
        r -= 1
    elif count > m:
        l = mid + 1
    elif count < m:
        r = mid - 1

print(mid)





