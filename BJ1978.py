n = int(input())
data = list(map(int, input().split()))
count = 0
flag = 0

for i in range(n):
    flag = 0
    if data[i] > 1:
        for j in range(2, data[i]):
            if data[i] % j == 0:
                flag = 1
                break

        if flag == 0:
            count += 1

print(count)

