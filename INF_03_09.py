n = int(input())
data = [[0 for i in range(n+2)] for j in range(n+2)]
count = 0

for i in range(1, n+1):
    data[i] = list(map(int, input().split()))
    data[i].append(0)
    data[i] = [0] + data[i]

for i in range(1, n+1):
    for j in range(1, n+1):
        if data[i][j] > data[i-1][j] and data[i][j] > data[i+1][j] and data[i][j] > data[i][j-1] and data[i][j] > data[i][j+1]:
            count += 1

print(count)