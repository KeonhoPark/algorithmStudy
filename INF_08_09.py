n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = data[0][0]


def dfs(row, col):
    if row == 0 and col == 0:
        return dp[0][0]
    if dp[row][col] != 0:
        return dp[row][col]
    else:
        if 0 <= row < n and 0 <= col < n:
            dp[row][col] = data[row][col] + min(dfs(row-1, col), dfs(row, col-1))
            return dp[row][col]
        else:
            return 1e9


dfs(n - 1, n - 1)
print(dp[n - 1][n - 1])
