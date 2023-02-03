n = int(input())
dp = dict()


def fibo(n):
    if n == 0 or n == 1:
        return n
    elif dp.get(n) is not None:
        return dp[n]
    else:
        if n % 2 == 0:
            sub_n = n // 2
            dp[sub_n - 1] = fibo(sub_n - 1) % 1000000007
            dp[sub_n] = fibo(sub_n) % 1000000007
            dp[n] = ((2 * dp[sub_n - 1] + dp[sub_n]) * dp[sub_n])
        else:
            sub_n = (n + 1) // 2
            dp[sub_n] = fibo(sub_n) % 1000000007
            dp[sub_n - 1] = fibo(sub_n - 1) % 1000000007
            dp[n] = (dp[sub_n] ** 2 + dp[sub_n - 1] ** 2)
        return dp[n]


print(fibo(n) % 1000000007)
print(dp)





