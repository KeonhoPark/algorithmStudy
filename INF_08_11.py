n = int(input())
coin = list(map(int, input().split()))
m = int(input())

dp = [1e9] * (m+1)
coin.sort()

dp[min(coin)] = 1
for i in range(min(coin)):
    dp[i] = 0

for c in coin:
    for j in range(c, len(dp)):
        dp[j] = min(dp[j-c]+1, dp[j])

print(dp[-1])