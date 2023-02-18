import sys


def row(col, x):
    for d in data[col]:
        if x == d:
            return False

    return True


def col(row, x):
    for i in range(9):
        if x == data[i][row]:
            return False

    return True


def square(col, row, x):
    for i in range(col, col + 3):
        for j in range(row, row + 3):
            if x == data[i][j]:
                return False

    return True


def dfs(l):
    if l == len(zeros):
        for i in range(9):
            print(*data[i])
        exit()
    else:
        z = zeros[l]
        for i in range(1, 10):
            if row(z[0], i) and col(z[1], i) and square((z[0] // 3) * 3, (z[1] // 3) * 3, i):
                data[z[0]][z[1]] = i
                dfs(l + 1)
                data[z[0]][z[1]] = 0


if __name__ == "__main__":
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    zeros = list()

    for i in range(9):
        for j in range(9):
            if data[i][j] == 0:
                zeros.append([i, j])

    dfs(0)
