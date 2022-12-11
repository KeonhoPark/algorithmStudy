import heapq

MAX = 1e9
max_heap = list()
res = list()

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        res.append(heapq.heappop(max_heap)[1])
    else:
        heapq.heappush(max_heap, [MAX - n, n])

if len(res) == 0:
    print(-1)
else:
    for x in res:
        print(x)


