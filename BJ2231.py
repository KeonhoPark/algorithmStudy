n = int(input())
flag = 0

for i in range(1, n+1):
    s = i
    a = i
    while i > 0:
        s += i % 10
        i = i // 10
    if s == n:
        print(a)
        flag = 1
        break

if flag == 0:
    print(0)