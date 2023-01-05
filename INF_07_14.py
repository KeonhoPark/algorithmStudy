import copy
from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_count = -1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def cluster(x, y, r):
    global count
    q = deque()
    area_copy[x][y] = 0
    q.append([x, y])
    while True:
        c = q.popleft()
        x = c[0]
        y = c[1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and area_copy[new_x][new_y] > r:
                area_copy[new_x][new_y] = 0
                q.append([new_x, new_y])
        if len(q) == 0:
            return


if __name__ == "__main__":
    for r in range(1, 101):
        area_copy = copy.deepcopy(area)
        count = 0
        for i in range(n):
            for j in range(n):
                if area_copy[i][j] > r:
                    cluster(i, j, r)
                    count += 1
        if count > max_count:
            max_count = count

    print(max_count)
