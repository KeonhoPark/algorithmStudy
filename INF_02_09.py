n = int(input())
data = [0 for i in range(n)]
price = [0 for i in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
    data[i].sort()

noon = 0
for i in range(n):
    count = 1
    for j in range(1, 3):
        if data[i][j-1] == data[i][j]:
            count += 1
            noon = data[i][j]

    if count == 3:
        price[i] = (noon*1000) + 10000
    elif count == 2:
        price[i] = (noon*100) + 1000
    else:
        price[i] = max(data[i])*100

print(max(price))

