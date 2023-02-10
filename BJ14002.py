import sys

n = int(input())
data = list(map(int, sys.stdin.readline().split()))

dp = [[1, [data[i]]] for i in range(n)]

for i in range(1, n):
    m = 0
    idx = -1
    for j in range(i):
        if data[j] < data[i] and m < dp[j][0]:
            m = dp[j][0]
            idx = j
    dp[i][0] = m + 1
    if idx != -1:
        dp[i][1] += dp[idx][1]

res = max(dp)
res[1].sort()
print(res[0])
print(*res[1])
