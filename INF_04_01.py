n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
l = 0
r = len(data)-1
mid = (l+r) // 2

while l <= r:
    mid = (l + r) // 2
    if data[mid] == m:
        print(mid+1)
        break
    elif data[mid] < m:
        l = mid+1
    elif data[mid] > m:
        r = mid-1


