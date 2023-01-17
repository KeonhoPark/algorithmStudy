n = int(input())
dp = [0] * (n + 1)


def dy(n):
    if n == 1 or n == 2:
        return n
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
        return dp[i]


print(dy(n))
