n, k = map(int, input().split())
data = list(map(int, input().split()))

data = sorted(data, reverse=True)
print(data[k-1])
