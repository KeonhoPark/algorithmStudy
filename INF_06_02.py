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


def dfs_front(root):
    visited_dfs[root] = 1
    print(root, end=" ")

    for i in range(1, 8):
        if matrix[root][i] == 1 and visited_dfs[i] == 0:
            dfs_front(i)


def dfs_mid(root):
    for i in range(1, 8):
        if matrix[root][i] == 1 and visited_dfs[i] == 0 and root * 2 == i:
            dfs_mid(i)

    visited_dfs[root] = 1
    print(root, end=" ")
    for j in range(1, 8):
        if matrix[root][j] == 1 and visited_dfs[j] == 0 and (root * 2) + 1 == j:
            dfs_mid(j)


def dfs_back(root):
    for i in range(1, 8):
        if matrix[root][i] == 1 and visited_dfs[i] == 0 and root < i:
            dfs_back(i)

    visited_dfs[root] = 1
    print(root, end=" ")


bfs_visited = [0] * 8




def bfs(root):
    bfs_queue = deque(list())
    bfs_queue.append(root)
    bfs_visited[root] = 1

    while bfs_queue:
        r = bfs_queue.popleft()
        print(r, end=" ")
        for i in range(1, 8):
            if matrix[r][i] == 1 and bfs_visited[i] == 0:
                bfs_queue.append(i)
                bfs_visited[i] = 1


visited_dfs = [0] * 8
dfs_front(1)
print()
visited_dfs = [0] * 8
dfs_mid(1)
print()
visited_dfs = [0] * 8
dfs_back(1)
print()
bfs(1)
