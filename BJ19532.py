import sys


def calc(a, b, c, d, e, f):
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if a*i + b*j == c and d*i + e*j == f:
                return i, j


a, b, c, d, e, f = map(int, sys.stdin.readline().split())
print(*calc(a, b, c, d, e, f))
