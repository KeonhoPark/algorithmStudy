n = int(input())
distance = list(map(int, input().split()))
gas = list(map(int, input().split()))
gas.pop()
data = list()
for i in range(n - 1):
    data.append([gas[i], distance[i]])

total = 0
min = 1e9
i = 0
while i < len(data):
    if data[i][0] < min:
        min = data[i][0]
    total += min * data[i][1]
    i += 1

print(total)
