data = list(input())
res = ''

for d in data:
    if d == 'U' or d == 'C' or d == 'P':
        res += d

flag = [0 for _ in range(4)]
f = 0
for r in res:
    if r == 'U':
        flag[0] = 1
    if r == 'C' and flag[0] == 1:
        flag[1] = 1
    if r == 'P' and flag[1] == 1:
        flag[2] = 1
    if r == 'C' and flag[2] == 1:
        flag[3] = 1

if sum(flag) == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
