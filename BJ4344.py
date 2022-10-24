c = int(input())

for i in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    count = 0
    sum = 0
    for j in range(1, n + 1):
        sum += data[j]
    avg = sum / n
    for k in range(1, n + 1):
        if data[k] > avg:
            count += 1
    print((format((count/n) * 100, ".3f"))+'%')

