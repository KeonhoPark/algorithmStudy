import sys


def fib(n):
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [0 for _ in range(40)]
    fib(n)
    print(dp[n - 1], n - 2, sep=" ")
