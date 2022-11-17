n = int(input())
weight = list(map(int, input().split()))
left = list()
right = list()
choo = [100, 50, 20, 10, 5, 2, 1]
left.append(weight[0])
right.append(weight[1])

for i in range(2, n):
    if sum(left) == sum(right):
        left.append(weight[i])
    else:
        if sum(left) > sum(right):
            right.append(weight[i])
        elif sum(left) < sum(right):
            left.append(weight[i])

weight_sub = abs(sum(left) - sum(right))

count = 0
for c in choo:
    if c == 1:
        count += weight_sub
        break
    while (weight_sub // c) != 0:
        count += (weight_sub // c)
        weight_sub = weight_sub % c

print(count)



