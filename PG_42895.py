def solution(n, number):
    dp = [[] for _ in range(9)]
    dp[1].append(n)
    dp[2] = [n * 10 + n, n + n, n - n, n * n, n // n]
    oper = ['+', '-', '*', '//']

    if number == n:
        return 1
    elif number in dp[2]:
        return 2
    else:
        for i in range(3, 9):
            for j in range(1, i):
                for o in oper:
                    for a in dp[j]:
                        for b in dp[i - j]:
                            if o == '+':
                                tmp = a + b
                                if tmp == number:
                                    return i
                                elif tmp >= 1 and tmp not in dp[i]:
                                    dp[i].append(tmp)
                            elif o == '-':
                                tmp = a - b
                                if tmp == number:
                                    return i
                                elif tmp >= 1 and tmp not in dp[i]:
                                    dp[i].append(tmp)
                            elif o == '*':
                                tmp = a * b
                                if tmp == number:
                                    return i
                                elif tmp >= 1 and tmp not in dp[i]:
                                    dp[i].append(tmp)
                            elif o == '//' and b != 0:
                                tmp = a // b
                                if tmp == number:
                                    return i
                                elif tmp >= 1 and tmp not in dp[i]:
                                    dp[i].append(tmp)

            dp[i].append(int(str(n) * i))

        return -1
