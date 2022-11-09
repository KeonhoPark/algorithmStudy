n, m = map(int, input().split())
sum = list()
f = [0 for _ in range(41)]
for i in range(1, n+1):
    for j in range(1, m+1):
        sum.append(i+j)

sum.sort()

for i in sum:
    f[i] += 1

for i in range(len(f)):
    if f[i] == max(f):
        print(i, end=" ")

