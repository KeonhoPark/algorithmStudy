data = [list(map(int, input().split())) for _ in range(10)]

dx = [1, -1, 0]
dy = [0, 0, -1]


def dfs(y, x):
    if y == 0:
        data[y][x] = 3
        return
    else:
        for i in range(3):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < 10 and 0 <= new_y < 10 and data[new_y][new_x] == 1:
                data[new_y][new_x] = 0
                b = dfs(new_y, new_x)
                break


for n in range(10):
    if data[9][n] == 2:
        dfs(9, n)

for k in range(10):
    if data[0][k] == 3:
        print(k)
