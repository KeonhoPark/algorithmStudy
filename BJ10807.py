n = int(input())
data = list(map(int, input().split()))
v = int(input())
count = 0

for i in range(len(data)):
    if data[i] == v:
        count += 1

print(count)
