import math

n = int(input())
data = [0]*(n+1)
count = 0
for i in range(2, int(math.sqrt(n))+1):
    if data[i] == 0:
        for j in range(i+i, n+1, i):
            data[j] = 1

for i in range(2, len(data)):
    if data[i] == 0:
        count += 1

print(count)


