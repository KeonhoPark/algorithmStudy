data = list()
n = int(input())
for i in range(n):
    data.append(int(input()))

data.sort()
for i in range(len(data)):
    print(data[i])