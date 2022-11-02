t = int(input())

for i in range(t):
    n = int(input())
    a = n // 2
    b = n // 2
    if a == 2:
        print(a, b)
    else:
        for j in range(a, 1, -1):
            for k in range(2, j):
                if j % k == 0:
                    break

            else:
                for k in range(2, b + (a-j)):
                    if (b + (a-j)) % k == 0:
                        break

                else:
                    b = b + (a - j)
                    a = j
                    print(a, b)
                    break

