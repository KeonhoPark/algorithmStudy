m = int(input())
n = int(input())
data = [10001 for i in range(10000)]
sum = 0
flag = 0

if n == 1:
    print(-1)

else:
    if m == 1:
        m += 1
    for i in range(m, n+1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            sum += i
            data.append(i)

    if sum != 0:
        print(sum)
        print(min(data))

    else:
        print(-1)




