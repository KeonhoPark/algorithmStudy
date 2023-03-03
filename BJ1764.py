import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
data1 = list()
data2 = list()
count = 0
res = list()
for _ in range(n):
    data1.append(sys.stdin.readline().strip())

for _ in range(m):
    data2.append(sys.stdin.readline().strip())

data1.sort()
data2.sort()
data1 = Counter(data1)
data2 = Counter(data2)

for d1 in data1:
    if d1 in data2:
        count += 1
        res.append(d1)

print(count)
for i in range(len(res)):
    print(res[i])
