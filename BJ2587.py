data = list()
for i in range(5):
    data.append(int(input()))

print(sum(data) // 5)
data = sorted(data)
print(data[2])
