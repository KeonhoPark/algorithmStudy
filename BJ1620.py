import sys

n, m = map(int, sys.stdin.readline().split())
data1 = dict()
data2 = dict()
for i in range(1, n + 1):
    name = sys.stdin.readline().strip()
    data1[i] = name
    data2[name] = i

for _ in range(m):
    p = sys.stdin.readline().strip()
    if p.isdecimal():
        print(data1.get(int(p)))
    else:
        print(data2.get(p))
