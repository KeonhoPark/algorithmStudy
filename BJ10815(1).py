import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
dic = dict()
for c in cards:
    dic[c] = 1

m = int(sys.stdin.readline())
prob = list(map(int, sys.stdin.readline().split()))
res = list()
for p in prob:
    if p in dic:
        res.append(1)
    else:
        res.append(0)

print(*res)
