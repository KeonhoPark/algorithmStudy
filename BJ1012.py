import sys
sys.setrecursionlimit(10 ** 6)


def cluster(y, x):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    data[y][x] = 0
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_y < c and 0 <= new_x < r and data[new_y][new_x] == 1:
            cluster(new_y, new_x)


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        r, c, n = map(int, sys.stdin.readline().split())
        data = [[0 for _ in range(r)] for _ in range(c)]
        for _ in range(n):
            j, i = map(int, sys.stdin.readline().split())
            data[i][j] = 1

        count = 0
        for i in range(c):
            for j in range(r):
                if data[i][j] == 1:
                    cluster(i, j)
                    count += 1

        print(count)
