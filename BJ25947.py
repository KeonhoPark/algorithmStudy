n, t, s = map(int, input().split())
item = list(map(int, input().split()))
count = 0

item.sort()

for i in range(len(item)):
    if t - item[i] <= 0:
        if t - (item[i] / 2) >= 0:
            t -= item[i] / 2
            count += 1
        else:
            break
    else:
        t -= item[i]
        count += 1


print(count)
