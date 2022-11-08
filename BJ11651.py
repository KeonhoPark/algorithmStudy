n = int(input())
data = [[0, 0] for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    data[i][0] = y
    data[i][1] = x

data.sort()
for i in range(len(data)):
    print(data[i][1], data[i][0], end=" ")
    print()