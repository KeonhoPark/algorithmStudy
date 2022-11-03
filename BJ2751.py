import sys

n = int(input())
data = list()

for i in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()

for i in range(len(data)):
    print(data[i])