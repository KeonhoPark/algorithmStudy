n = int(input())
data = [[0 for i in range(100)] for j in range(n)]
flag = [[0 for i in range(26)] for j in range(n)]
f = True
count = 0

for i in range(n):
    data[i] = list(input())
    flag[i][ord(data[i][0]) - 97] = 1
    for j in range(1, len(data[i])):
        if data[i][j] != data[i][j-1]:
            flag[i][ord(data[i][j]) - 97] += 1

for i in range(n):
    for j in range(len(flag[i])):
        if flag[i][j] > 1:
            f = False
            break
        else:
            f = True
    if f:
        count += 1

print(count)
