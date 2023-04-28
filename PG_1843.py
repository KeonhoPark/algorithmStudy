def solution(arr):
    INF = 1e9
    n = 0
    for a in arr:
        if a != '+' and a != '-':
            n += 1

    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]

    for distance in range(n):
        for i in range(n - distance):
            j = distance + i

            if distance == 0:
                MAX_DP[i][i] = int(arr[i * 2])
                MIN_DP[i][i] = int(arr[i * 2])

            else:
                for k in range(i, j):
                    if arr[2 * k + 1] == '+':
                        MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k + 1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k + 1][j])
                    elif arr[2 * k + 1] == '-':
                        MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k + 1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k + 1][j])

    return MAX_DP[0][-1]
