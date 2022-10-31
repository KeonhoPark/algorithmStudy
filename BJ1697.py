from collections import deque

r, e = map(int, input().split())
MAX = 100000
check = [0 for i in range(MAX+1)]
dis = [0 for i in range(MAX+1)]
check[r] = 1
dis[r] = 0
queue = deque()
queue.append(r)
while queue:
    now = queue.popleft()
    if now == e:
        break
    for next in (now-1, 2*now, now+1):
        if 0 <= next <= MAX:
            if check[next] == 0:
                queue.append(next)
                check[next] = 1
                dis[next] = dis[now]+1

print(dis[e])
