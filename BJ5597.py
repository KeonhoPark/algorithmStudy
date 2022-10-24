data = [0 for i in range(31)]

for i in range(28):
    n = int(input())
    data[n] = n

for j in range(1, 31):
    if data[j] == 0:
        print(j)
