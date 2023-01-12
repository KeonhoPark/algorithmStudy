n, m = map(int, input().split())
dp = [0] * (m + 1)
stone = list()
for _ in range(n):
    stone.append(list(map(int, input().split())))

for i in range(len(stone)):
    w = stone[i][0]
    v = stone[i][1]
    for j in range(w, m + 1):
        dp[j] = max(dp[j - w] + v, dp[j])

print(dp[m])
