n = int(input())
data = list(map(int, input()))
sum = 0

for i in range(n):
    sum += data[i]

print(sum)