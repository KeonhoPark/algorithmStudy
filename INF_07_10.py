data = [0 for _ in range(7)]
for i in range(7):
    data[i] = list(map(int, input().split()))

visited = [[0 for _ in range(7)] for _ in range(7)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0


def dfs(x, y):
    global count
    if x == 6 and y == 6:
        count += 1
        return
    else:
        visited[x][y] = 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x <= 6 and 0 <= new_y <= 6:
                if visited[new_x][new_y] == 0 and data[new_x][new_y] == 0:
                    dfs(new_x, new_y)
                    visited[new_x][new_y] = 0


dfs(0, 0)
print(count)


