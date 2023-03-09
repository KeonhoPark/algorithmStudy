import sys

n = int(sys.stdin.readline())

if n == 1:
    print(0)
    print(1)

elif n == 2:
    print(1)
    print('2 1')

elif n == 3:
    print(1)
    print('3 1')

else:
    dp = [[0, [i]] for i in range(n + 1)]

    dp[2] = [1, [2, 1]]
    dp[3] = [1, [3, 1]]

    for i in range(4, n + 1):
        pre = list()
        pre.append(dp[i - 1])
        if i % 2 == 0:
            pre.append(dp[i // 2])
        if i % 3 == 0:
            pre.append(dp[i // 3])

        mn = min(pre)
        dp[i][0] = mn[0] + 1
        dp[i][1] += mn[1]

    print(dp[n][0])
    print(*dp[n][1])

