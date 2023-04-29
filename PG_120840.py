def solution(n, m):
    dp = [0 for _ in range(31)]
    dp[1] = 1

    for i in range(2, 31):
        dp[i] = dp[i - 1] * i

    if n == m:
        return 1
    else:
        return dp[n] // (dp[n - m] * dp[m])
