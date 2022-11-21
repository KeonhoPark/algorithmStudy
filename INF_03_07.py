n = int(input())
data = [[] for i in range(n)]
sum = 0

for i in range(n):
    data[i] = list(map(int, input().split()))

for i in range(n):
    num = int(abs(i - ((n-1)/2)))
    for j in range(num, n-num):
        sum += data[i][j]

print(sum)