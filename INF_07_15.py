from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
flag = 0

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])


while True:
    c_list = list()
    if len(q) == 0:
        break

    while len(q) != 0:
        c_list.append(q.popleft())

    count += 1

    for c in c_list:
        x = c[1]
        y = c[0]
        s = 0
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < m and 0 <= new_y < n and tomato[new_y][new_x] == 0:
                tomato[new_y][new_x] = 1
                q.append([new_y, new_x])


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            flag = 1
            break
    if flag == 1:
        break

else:
    print(count-1)
