if __name__=="__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    if m < min(coin):
        print(-1)
    else:
        dp = [1e9] * (m+1)

        for c in coin:
            for j in range(c, len(dp)):
                dp[j] = min(dp[j-c]+1, dp[j])

        print(dp[-1])