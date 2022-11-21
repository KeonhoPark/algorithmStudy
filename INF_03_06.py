n = int(input())
data = [[]]*n
row = list()
column = list()
dae = list()
ans = list()

for i in range(n):
    data[i] = list(map(int, input().split()))

for i in range(n):
    row.append(sum(data[i]))

for i in range(n):
    sum = 0
    for j in range(n):
        sum += data[j][i]
    column.append(sum)

sum_1 = 0
sum_2 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum_1 += data[i][j]
            sum_2 += data[i][n-j-1]
dae.append(sum_1)
dae.append(sum_2)

row.sort(reverse=True)
column.sort(reverse=True)
dae.sort(reverse=True)
ans.append(row[0])
ans.append(column[0])
ans.append(dae[0])
ans.sort(reverse=True)
print(ans[0])