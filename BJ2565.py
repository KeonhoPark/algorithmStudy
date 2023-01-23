n = int(input())
data = [0] * 501
for i in range(n):
    s, e = map(int, input().split())
    data[s] = e

dp = [1] * 501


def dy(n):
    if n == 1:
        return 0
    elif dp[n] != 1:
        return dp[n]
    else:
        dp[1] = 1
        for i in range(2, len(dp)):
            m = -1
            for j in range(1, i):
                if data[i] > data[j] and m < dp[j]:
                    m = dp[j]
            dp[i] = m + 1
        return dp[n]


dy(n)
print(dp)
print(max(dp))

