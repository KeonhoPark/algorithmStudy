data = list(i for i in range(1, 21))
for i in range(10):
    s, e = map(int, input().split())
    temp = 0
    while s < e:
        temp = data[s-1]
        data[s-1] = data[e-1]
        data[e-1] = temp
        s += 1
        e -= 1

for i in range(len(data)):
    print(data[i], end=" ")