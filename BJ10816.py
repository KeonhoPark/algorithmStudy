import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

card.sort()
count = dict()

for c in card:
    if count.get(c) is None:
        count[c] = 1
    else:
        count[c] += 1

res = list()

for d in data:
    s = 0
    e = len(card) - 1
    flag = 0
    while s <= e:
        mid = (s + e) // 2
        if d == card[mid]:
            res.append(count[d])
            flag = 1
            break
        elif d < card[mid]:
            e = mid - 1
        else:
            s = mid + 1

    if flag == 0:
        res.append(0)

print(*res)
