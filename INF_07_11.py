n = int(input())
data = [0 for _ in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))

data_max = max(list(map(max, data)))
data_min = min(list(map(min, data)))

visited = [[0 for _ in range(n)] for _ in range(n)]
count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count
    if data[x][y] == data_max:
        count += 1
        return
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if visited[new_x][new_y] == 0 and data[x][y] < data[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    dfs(new_x, new_y)
                    visited[new_x][new_y] = 0


min_x = 0
min_y = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == data_min:
            min_x = i
            min_y = j
dfs(min_x, min_y)
print(count)
