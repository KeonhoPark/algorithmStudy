import sys
import heapq

s, e = map(int, sys.stdin.readline().split())
q = []
heapq.heappush(q, [0, [s]])
MAX = 100001
res = [-1 for _ in range(MAX)]
res[s] = 0

if s > e:
    print(s - e)
    tmp = []
    for i in range(s, e - 1, -1):
        tmp.append(i)
    print(*tmp)

else:
    while q:
        time, pos_his = heapq.heappop(q)
        if pos_his[-1] == e:
            print(time)
            print(*pos_his)
            break

        else:
            next_pos = -1
            for i in range(3):
                if i == 0:
                    next_pos = pos_his[-1] * 2
                elif i == 1:
                    next_pos = pos_his[-1] + 1
                else:
                    next_pos = pos_his[-1] - 1

                if not (0 <= next_pos < MAX):
                    continue

                if res[next_pos] != -1 and res[next_pos] <= res[pos_his[-1]]:
                    continue

                heapq.heappush(q, [time + 1, pos_his + [next_pos]])
                res[next_pos] = time + 1
