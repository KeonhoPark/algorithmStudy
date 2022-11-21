n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
total = 0


for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if data[i] + data[j] + data[k] > m:
                continue
            else:
                total = max(total, data[i] + data[j] + data[k])


print(total)

