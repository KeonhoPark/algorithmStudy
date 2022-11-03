import sys

n = int(input())
data = [0 for i in range(-4000, 4001, 1)]
sum = 0
pos = (n//2)+1
median = 0
flag = 0
frequent = 0
f = list()
new_data = list()

for i in range(n):
    data[(int(sys.stdin.readline()))] += 1

frequent = sorted(data, reverse=True)[0]

for i in range(-4000, 4001, 1):
    if data[i] != 0:
        sum += (i*data[i])
        pos -= data[i]
        if pos <= 0 and flag == 0:
            median = i
            flag = 1
        if frequent == data[i]:
            f.append(i)

for i in range(-4000, 4001, 1):
    for j in range(data[i]):
        new_data.append(i)



print(round(sum/n))
print(median)
if len(f) == 1:
    print(f[0])
else:
    print(f[1])
print(new_data[len(new_data)-1] - new_data[0])




