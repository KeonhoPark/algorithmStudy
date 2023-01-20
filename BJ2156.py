n = int(input())
data = [0]
for i in range(n):
    data.append(int(input()))

dp = [0 for _ in range(n+1)]


def dy(n):
    if n == 1:
        return data[1]
    elif n == 2:
        return data[1] + data[2]
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[1] = data[1]
        dp[2] = data[1] + data[2]
        for i in range(3, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])
        return dp[n]


print(dy(n))
