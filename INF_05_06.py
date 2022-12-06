from collections import deque

n, m = map(int, input().split())
data = [x for x in enumerate(list(map(int, input().split())))]
data = deque(data)

count = 0
while len(data) > 0:
    first = data.popleft()

    if any(first[1] < d[1] for d in data):
        data.append(first)

    else:
        count += 1
        if first[0] == m:
            break

print(count)

