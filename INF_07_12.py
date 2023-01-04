from collections import deque

n = int(input())
house = [[0] for _ in range(n)]
for i in range(n):
    house[i] = list(map(int, input()))

hn_list = list()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
danji_num = 0
bfs_visited = [[0 for _ in range(n)] for _ in range(n)]
dfs_visited = [[0 for _ in range(n)] for _ in range(n)]
start_list = list()


def cluster(x, y, danji_num):
    q = deque()
    house_count = 0
    if check_visited(x, y):
        return

    if house[x][y] == 1:
        bfs_visited[x][y] = danji_num
        house_count += 1
        q.append([x, y])
    while True:
        c = q.popleft()
        x = c[0]
        y = c[1]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if house[new_x][new_y] == 1 and bfs_visited[new_x][new_y] == 0:
                    bfs_visited[new_x][new_y] = danji_num
                    house_count += 1
                    q.append([new_x, new_y])

        if len(q) == 0:
            hn_list.append(house_count)
            break


def check_visited(x, y):
    if bfs_visited[x][y] == 0:
        return False
    else:
        return True


def find_start(x, y):
    global danji_num
    if x == n - 1 and y == n - 1:
        return
    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if house[new_x][new_y] == 1 and house[x][y] == 0 and dfs_visited[new_x][new_y] == 0:
                    if not check_visited(new_x, new_y):
                        danji_num += 1
                    cluster(new_x, new_y, danji_num)
                if dfs_visited[new_x][new_y] == 0:
                    dfs_visited[new_x][new_y] = 1
                    find_start(new_x, new_y)


find_start(0, 0)
print(danji_num)
hn_list.sort()
print(*hn_list, sep='\n')
