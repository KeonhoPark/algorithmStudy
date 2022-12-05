from collections import deque

n, k = map(int, input().split())
data = list()

for i in range(1, n+1):
    data.append(i)

queue = deque(data)

# i = 0
# count = 1
# while len(data) > 1:
#     count += 1
#     i += 1
#     if count == k:
#         if i > len(data) - 1:
#             i = i % len(data)
#         data.pop(i)
#         count = 1
#
# print(data[0])

count = 1
while len(queue) > 1:
    if count == k:
        queue.popleft()
        count = 0
    else:
        d = queue.popleft()
        queue.append(d)
    count += 1

print(queue[0])
