a_list = list(input())
b_list = list(input())
a = len(a_list)
b = len(b_list)
dp = [[0] * (b+1) for _ in range(a+1)]
print(dp)

for i in range(1, a+1):
    for j in range(1, b+1):
        if a_list[i-1] == b_list[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])

