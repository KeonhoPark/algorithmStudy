k, n = map(int, input().split())
data = list()
for i in range(k):
    data.append(int(input()))

data.sort(reverse=True)
l = 1
r = data[0]

while l <= r:
    count = 0
    m = (l + r) // 2
    for d in data:
        count += d // m
    if count < n:
        r = m - 1
    elif count >= n:
        l = m + 1
        res = m

print(res)
