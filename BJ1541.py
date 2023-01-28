data = list(input().split(sep='-'))

for i in range(len(data)):
    new_d = data[i].split(sep='+')
    if len(new_d) != 1:
        for j in range(len(new_d)):
            new_d[j] = int(new_d[j])
        data[i] = sum(new_d)
    data[i] = int(data[i])

sum = data[0]
for i in range(1, len(data)):
    sum -= data[i]

print(sum)


