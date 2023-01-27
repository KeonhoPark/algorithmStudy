n = int(input())
data = [[0, 0] for _ in range(n)]
count = 0

for i in range(n):
    s, e = map(int, input().split())
    data[i][0] = s
    data[i][1] = e

data.sort(key=lambda x: (x[1], x[0]))

e = -1
for i in range(len(data)):
    if e <= data[i][0]:
        count += 1
        e = data[i][1]

print(data)
print(count)


