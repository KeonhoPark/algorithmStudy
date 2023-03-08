import sys
import heapq

MAX = int(1e9)


def djikstra(q, dist):

    while q:
        cur_dis, start, next_pos = heapq.heappop(q)

        if start == next_pos:
            return dist[start][next_pos]

        # if dist[start][next_pos] < cur_dis:
        #     continue

        for next_n_pos, next_n_dis in data[next_pos]:
            tmp = cur_dis + next_n_dis
            if tmp < dist[start][next_n_pos]:
                dist[start][next_n_pos] = tmp
                heapq.heappush(q, (tmp, start, next_n_pos))

    return MAX


n, e = map(int, sys.stdin.readline().split())
data = [[] for _ in range(n + 1)]
q = []
dist = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    data[a].append([b, w])
    heapq.heappush(q, (w, a, b))
    dist[a][b] = w

ans = djikstra(q, dist)
if ans != MAX:
    print(ans)
else:
    print(-1)
