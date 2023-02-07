n, m = map(int, input().split())
matrix1 = [list(map(int, input())) for _ in range(n)]
matrix2 = [list(map(int, input())) for _ in range(n)]


def compare(y, x):
    if matrix1[y][x] != matrix2[y][x]:
        return False
    else:
        return True


def transpose(y, x):
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            if matrix1[i][j] == 0:
                matrix1[i][j] = 1
            else:
                matrix1[i][j] = 0


count = 0
if n < 3 or m < 3:
    if matrix1 == matrix2:
        print(0)
    else:
        print(-1)

elif n == 3 and m == 3:
    if matrix1 == matrix2:
        print(0)
    else:
        transpose(0, 0)
        if matrix1 != matrix2:
            print(-1)
        else:
            print(1)

else:
    if matrix1 == matrix2:
        print(0)
    else:
        for i in range(n - 2):
            for j in range(m - 2):
                if not compare(i, j):
                    transpose(i, j)
                    count += 1

        if matrix1 != matrix2:
            print(-1)
        else:
            print(count)

