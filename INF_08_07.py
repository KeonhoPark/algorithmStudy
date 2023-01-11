n = int(input())
brick = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    brick[i] = list(map(int, input().split()))

brick.sort()
dp = [brick[i][1] for i in range(n)]

for i in range(n):
    m = 0
    m_idx = 0
    for j in range(i):
        if brick[i][2] > brick[j][2] and dp[j] > m:
            m = dp[j]
            m_idx = j
    dp[i] += m

print(max(dp))





