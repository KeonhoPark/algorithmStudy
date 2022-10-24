white = [[0 for i in range(100)] for j in range(100)]
loc = [[0, 0] for i in range(100)]
n = int(input())
count = 0

for i in range(n):
    loc[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(loc[i][1], loc[i][1] + 10):
        for k in range(loc[i][0], loc[i][0] + 10):
            white[j][k] = 1

for i in range(100):
    for j in range(100):
        if white[i][j] == 1:
            count += 1

print(count)