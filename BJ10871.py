n, x = map(int, input().split())
data = [0 for i in range(n)]
ans = []

data = list(map(int, input().split()))

for i in range(n):
    if data[i] < x:
        print(data[i], end=" ")


