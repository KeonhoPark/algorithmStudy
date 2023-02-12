import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
tree = Counter(map(int, sys.stdin.readline().split()))

s = 0
e = max(tree)

while s <= e:
    mid = (s + e) // 2
    total = 0

    for t in tree:
        if t > mid:
            total += (t - mid) * tree[t]

    if total >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)





