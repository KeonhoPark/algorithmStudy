import sys

data1 = list(sys.stdin.readline().strip())
data2 = list(sys.stdin.readline().strip())
dp = [['' for _ in range(len(data1) + 1)] for _ in range(len(data2) + 1)]

res = list()
for i in range(1, len(data2) + 1):
    for j in range(1, len(data1) + 1):
        if data2[i - 1] == data1[j - 1]:
            dp[i][j] = dp[i-1][j-1] + data2[i - 1]

        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

for i in range(len(dp)):
    print(dp[i])
print(len(dp[-1][-1]))
print(dp[-1][-1])
