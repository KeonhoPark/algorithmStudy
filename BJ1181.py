n = int(input())
data = [[] for i in range(n)]

for i in range(n):
    word = input()
    data[i].append(len(word))
    data[i].append((word))

data.sort()

i = 1
while i < len(data):
    if data[i-1] == data[i]:
        data.pop(i)
    else:
        i += 1

for i in range(len(data)):
    print(data[i][1])