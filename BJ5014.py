from collections import deque

floor, start, go, up, down = map(int, input().split())

MAX = 1000000
check = [0 for i in range(MAX+1)]
dis = [-1 for i in range(MAX+1)]
check[start] = 1
dis[start] = 0
flag = 0

queue = deque()
queue.append(start)
while queue:
    now = queue.popleft()
    if now == go:
        break
    for next in (now - down, now + up):
        if 1 <= next <= floor:
            if check[next] == 0:
                queue.append(next)
                check[next] = 1
                dis[next] = dis[now] + 1

if dis[go] != -1:
    print(dis[go])
else:
    print('use the stairs')




