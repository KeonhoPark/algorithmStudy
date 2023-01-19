n = int(input())
dp = [0] * (n+1)


def dy(n):
    global dp
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[1] = 0
        dp[2] = dp[3] = 1
        for i in range(4, n+1):
            if i % 2 != 0 and i % 3 != 0:
                dp[i] = dp[i-1] + 1
            if i % 2 == 0 and i % 3 == 0:
                dp[i] += min(dp[i // 3] + 1, dp[i - 1] + 1, dp[i // 2] + 1)
                continue
            if i % 3 == 0:
                dp[i] += min(dp[i // 3] + 1, dp[i - 1] + 1)
            elif i % 2 == 0:
                dp[i] += min(dp[i // 2] + 1, dp[i - 1] + 1)
        return dp[n]


print(dy(n))

