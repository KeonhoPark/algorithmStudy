import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
MAX = sys.maxsize
graph = [[] for _ in range(n + 1)]
dist = [MAX for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))

s, e = map(int, sys.stdin.readline().split())

heap = []
heapq.heappush(heap, (0, s, [s]))
dist[s] = 0

while heap:
    print(heap)
    print(dist)
    cost, cur_pos, route = heapq.heappop(heap)
    if cur_pos == e:
        print(cost)
        print(len(route))
        print(*route)
        break

    if dist[cur_pos] < cost:
        continue

    for next_pos, c in graph[cur_pos]:
        if dist[next_pos] > dist[cur_pos] + c:
            heapq.heappush(heap, (cost + c, next_pos, route + [next_pos]))
            dist[next_pos] = cost + c


# import sys
# import heapq
#
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# graph = [[] for _ in range(n + 1)]
# dist = [-1 for _ in range(n + 1)]
#
# for _ in range(m):
#     s, e, c = map(int, sys.stdin.readline().split())
#     graph[s].append([e, c])
#
# s, e = map(int, sys.stdin.readline().split())
#
# heap = []
# heapq.heappush(heap, [0, s, [s]])
# dist[s] = 0
#
# while heap:
#     print(heap)
#     print(dist)
#     cost, cur_pos, route = heapq.heappop(heap)
#     if cur_pos == e:
#         print(cost)
#         print(len(route))
#         print(*route)
#         break
#
#     # if dist[cur_pos]
#
#     for next_pos, c in graph[cur_pos]:
#         if dist[next_pos] != -1 and dist[next_pos] <= dist[cur_pos] + c:
#             continue
#
#         heapq.heappush(heap, [cost + c, next_pos, route + [next_pos]])
#         dist[next_pos] = dist[cur_pos] + c
#
