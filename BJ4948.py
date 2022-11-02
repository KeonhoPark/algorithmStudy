import math

MAX = 123456
data = [0 for i in range(2*MAX+1)]

for i in range(2, 2*MAX+1):
    flag = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        data[i] = 1

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if data[i] == 1:
            count += 1

    print(count)
