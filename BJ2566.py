data = [[0 for i in range(9)] for j in range(9)]
max = 0
n = 0
m = 0

for i in range(9):
    data[i] = list(map(int, input().split()))

for i in range(9):
    for j in range(9):
        if data[i][j] >= max:
            max = data[i][j]
            n = i + 1
            m = j + 1

print(max)
print(n, m)