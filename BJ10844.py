n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]

for i in range(1, len(dp[1])):
    dp[1][i] = 1


def dy(n):
    if n == 1:
        return 9
    else:
        for i in range(2, n+1):
            for j in range(10):
                if j == 0:
                    dp[i][j] = dp[i-1][1]
                elif j == 9:
                    dp[i][j] = dp[i-1][8]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        return sum(dp[n])


print(dy(n) % 1000000000)
