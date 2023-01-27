n = int(input())
data = list(map(int, input().split()))
t = 0

data.sort()

for i in range(len(data)):
    s = 0
    for j in range(i+1):
        s += data[j]
    t += s

print(t)

