import heapq
import sys


def djikstra(s):
    q = []
    heapq.heappush(q, (0, s))
    res = [-1 for _ in range(MAX+1)]
    res[s] = 0

    while q:
        time, cur_pos = heapq.heappop(q)
        print(time, cur_pos)
        if cur_pos == e:
            return res[cur_pos]

        for i in range(3):
            if i == 0:
                next_pos = cur_pos + 1
            elif i == 1:
                next_pos = cur_pos - 1
            else:
                next_pos = cur_pos * 2

            if not (0 <= next_pos < MAX):
                continue
            if res[next_pos] != -1 and res[next_pos] <= res[cur_pos]:
                continue

            if i < 2:
                heapq.heappush(q, (time + 1, next_pos))
                res[next_pos] = time + 1
            else:
                heapq.heappush(q, (time, next_pos))
                res[next_pos] = time


MAX = 100001
s, e = map(int, sys.stdin.readline().split())
print(djikstra(s))
