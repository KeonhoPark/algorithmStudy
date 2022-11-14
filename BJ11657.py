import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edges = list()
time = [INF] * n


def bf(start):
    time[start] = 0

    for i in range(1, n + 1):
        for j in range(m):
            now, next, t = edges[j][0], edges[j][1], edges[j][2]
            if time[now] != INF and time[next] > time[now] + t:
                time[next] = time[now] + t
                if i == n:
                    return True
    return False


for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bf(1)

print(time)
print(edges)

if negative_cycle == True:
    print(-1)
else:
    for i in range(2, n + 1):
        if time[i] == INF:
            print(-1)
        else:
            print(time[i])
