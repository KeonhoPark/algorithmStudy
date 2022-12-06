from collections import deque

n, m = map(int, input().split())
data = deque((map(int, input().split())))

index = m
count = 1
while len(data) > 0:
    max = 0
    first = data[0]
    if index == n:
        index -= n

    for i in range(1, len(data)):
        if data[i] > max:
            max = data[i]

    if first < max:
        data.popleft()
        data.append(first)
        if index == 0:
            index = len(data)-1
        else:
            index -= 1

    else:
        data.popleft()
        if index == 0:
            break
        else:
            count += 1
            index -= 1


print(count)

