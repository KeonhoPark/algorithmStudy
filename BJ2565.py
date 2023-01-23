n = int(input())
data = [0] * 501
m = 0
for i in range(n):
    s, e = map(int, input().split())
    if s > m:
        m = s
    data[s] = e
dp = [0] * 501

for i in range(1, m+1):
    mx = 0
    if data[i] == 0:
        dp[i] = 0
    else:
        for j in range(1, i):
            if data[i] > data[j] and mx < dp[j]:
                mx = dp[j]
        dp[i] = mx + 1

print(n - max(dp))


