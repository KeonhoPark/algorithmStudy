import sys
import heapq


def djikstra(s):
    q = []
    heapq.heappush(q, [0, s])
    result = [1e9 for _ in range(n + 1)]
    result[s] = 0

    while q:
        cur_dist, cur_pos = heapq.heappop(q)

        for next_pos, next_dist in data[cur_pos]:
            tmp = cur_dist + next_dist
            if tmp < result[next_pos]:
                heapq.heappush(q, [tmp, next_pos])
                result[next_pos] = tmp

    return result


T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    data = [[] for _ in range(n + 1)]
    res = list()

    for i in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        data[a].append([b, d])
        data[b].append([a, d])

    s_ = djikstra(s)
    g_ = djikstra(g)
    h_ = djikstra(h)

    for _ in range(t):
        cand = int(sys.stdin.readline())

        if s_[cand] == s_[g] + g_[h] + h_[cand] or s_[cand] == s_[h] + h_[g] + g_[cand]:
            res.append(cand)

    res.sort()
    print(*res)
