n, m = map(int, input().split())
problem = list()
problem.sort()

for i in range(n):
    problem.append(list(map(int, input().split())))

dp = [0] * (m+1)
for i in range(len(problem)):
    score = problem[i][0]
    time = problem[i][1]
    for j in range(m, time-1, -1):
        dp[j] = max(dp[j-time] + score, dp[j])


print(dp)
print(dp[m])
