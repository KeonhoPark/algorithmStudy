import sys

n, t, s = map(int, sys.stdin.readline().split())
item = list(map(int, sys.stdin.readline().split()))
item.sort()

start = 0
end = 0
total = 0

for i in range(len(item)):
    if end - start < s:
        item[end] //= 2
        total += item[end]
        end += 1

    elif end - start == s:
        item[end] //= 2
        total += (item[end] + item[start])
        item[start] *= 2
        end += 1
        start += 1

    # print(item)
    # print(total)

    if total > t:
        print(i)
        break
    elif total == t:
        print(i + 1)
        break

else:
    print(i + 1)
