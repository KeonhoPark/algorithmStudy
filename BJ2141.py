import sys

n = int(input())
data = list()
total = 0
for i in range(n):
    v, p = map(int, sys.stdin.readline().split())
    total += p
    data.append([v, p])

data.sort(key=lambda x: x[0])
h = total / 2
print(h)
count = 0
for d in data:
    count += d[1]
    if count >= h:
        print(d[0])
        break
