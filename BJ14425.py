import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
data = list()
prob = list()
count = 0
for _ in range(n):
    data.append(sys.stdin.readline().strip())

for _ in range(m):
    prob.append(sys.stdin.readline().strip())

data = Counter(data)
prob = Counter(prob)

for d in data:
    if d in prob:
        count += prob.get(d)

print(count)


