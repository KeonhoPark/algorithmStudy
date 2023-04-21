def solution(triangle):
    n = len(triangle)
    dp = [[] for _ in range(n)]
    dp[0] = triangle[0]
    dp[1] = [triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]]

    for i in range(2, n):
        for j in range(len(dp[i - 1]) + 1):
            l = len(dp[i - 1])
            print(l)
            if j == 0:
                dp[i].append(dp[i - 1][0] + triangle[i][0])
            elif j == l:
                dp[i].append(dp[i - 1][j - 1] + triangle[i][l])
            else:
                dp[i].append(max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j])

    print(dp)
    return max(dp[-1])

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
