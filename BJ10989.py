import sys

n = int(sys.stdin.readline())
data = [0 for i in range(10001)]

for i in range(n):
    t = int(sys.stdin.readline())
    data[t] += 1

for i in range(len(data)):
    for j in range(data[i]):
        print(i)