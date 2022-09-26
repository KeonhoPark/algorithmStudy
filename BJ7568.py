number = int(input())

data = []
rank = []

for i in range(number):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(number):
    count = 0
    for j in range(number):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count + 1)

for d in rank:
    print(d, end=" ")




