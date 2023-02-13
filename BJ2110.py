import sys

n, c = map(int, sys.stdin.readline().split())
house = list()
for _ in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

s = 1
e = house[-1] - house[0]

if n == 2:
    print(e)
else:
    while s <= e:
        mid = (s + e) // 2
        count = 1
        h = house[0]
        for i in range(n):
            if house[i] - h > mid:
                count += 1
                h = house[i]

        if count >= c:
            s = mid + 1
        elif count < c:
            e = mid - 1

    print(s)











