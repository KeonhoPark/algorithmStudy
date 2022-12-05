n, k = map(int, input().split())
data = list()
for i in range(1, n+1):
    data.append(i)

i = 0
count = 1
while len(data) > 1:
    count += 1
    i += 1
    if count == k:
        if i > len(data) - 1:
            i = i % len(data)
        data.pop(i)
        count = 1

    # if i > len(data)-1:
    #     count += 1
    #     i = 0

print(data[0])
