import sys
from collections import Counter

m, n = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a = Counter(a)
b = Counter(b)

print(len(a - b) + len(b - a))
