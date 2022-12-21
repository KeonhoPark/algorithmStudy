from collections import deque

matrix = [[0] * 8 for _ in range(8)]

for i in range(8):
    matrix[i][i] = 1

matrix[1][2] = matrix[2][1] = 1
matrix[1][3] = matrix[3][1] = 1
matrix[2][4] = matrix[4][2] = 1
matrix[2][5] = matrix[5][2] = 1
matrix[3][6] = matrix[6][3] = 1
matrix[3][7] = matrix[7][3] = 1

dfs_visited = [0] * 8
bfs_visited = [0] * 8


def dfs(root):
    dfs_visited[root] = 1
    print(root, end=" ")
    for i in range(1, 8):
        if matrix[root][i] == 1 and dfs_visited[i] == 0:
            dfs(i)


def bfs(root):
    bfs_visited[root] = 1
    bfs_queue = deque(list())
    bfs_queue.append(root)
    while bfs_queue:
        r = bfs_queue.popleft()
        print(r, end=" ")
        for i in range(1, 8):
            if matrix[r][i] == 1 and bfs_visited[i] == 0:
                bfs_queue.append(i)
                bfs_visited[i] = 1


dfs(1)
print()
bfs(1)
