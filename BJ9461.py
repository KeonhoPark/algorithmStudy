t = int(input())
dp = [0] * 101
for i in range(1, 4):
    dp[i] = 1


def dy(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]
        return dp[i]


for _ in range(t):
    n = int(input())
    print(dy(n))



