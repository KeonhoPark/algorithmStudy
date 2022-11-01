import math

m, n = map(int, input().split())
flag = 0

if m == 1:
    m += 1
for i in range(m, n+1):
    flag = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)

