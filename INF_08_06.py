n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp.insert(0, 1)

for i in range(len(data)):
    m = 0
    for j in range(i):
        if data[i] > data[j] and dp[j] > m:
            m = dp[j]
    dp[i] = m + 1

print(max(dp))






