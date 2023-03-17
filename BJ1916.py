import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
dist = [-1 for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append([e, c])

s, e = map(int, sys.stdin.readline().split())

heap = []
heapq.heappush(heap, [0, s])
dist[s] = 0

while heap:
    print(heap)
    print(dist)
    cost, cur_pos = heapq.heappop(heap)
    if cur_pos == e:
        print(cost)
        break

    for next_pos, c in graph[cur_pos]:
        if dist[next_pos] != -1 and dist[next_pos] <= dist[cur_pos] + c:
            continue

        heapq.heappush(heap, [cost + c, next_pos])
        dist[next_pos] = dist[cur_pos] + c
