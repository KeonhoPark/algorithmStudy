import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
prob = list(map(int, sys.stdin.readline().split()))
res = list()

cards = Counter(cards)
for p in prob:
    if p in cards:
        res.append(1)
    else:
        res.append(0)

print(*res)
