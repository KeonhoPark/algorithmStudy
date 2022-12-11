import heapq

min_heap = list()
res = list()

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        res.append(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, n)

for x in res:
    print(x)

ans = list()
while True:
    n = int(input())
    if n == -1:
        break
    else:
        ans.append(n)

if res == ans:
    print("True")
else:
    print("False")
