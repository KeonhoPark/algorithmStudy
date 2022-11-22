n = int(input())
data = [0 for i in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))

m = int(input())
order = [0 for i in range(m)]

for i in range(m):
    r, d, a = map(int, input().split())
    r -= 1
    tmp = data[r].copy()
    for j in range(n):
        if d == 0:
            if j >= a:
                data[r][j-a] = tmp[j]
            else:
                data[r][n-(abs(j-a))] = tmp[j]
        elif d == 1:
            data[r][(j+a) % n] = tmp[j]


mean = (n-1) // 2
sum = 0
for i in range(n):
    for j in range(mean - abs(i - mean), mean + abs(i - mean) + 1):
         sum += data[i][j]

print(sum)

