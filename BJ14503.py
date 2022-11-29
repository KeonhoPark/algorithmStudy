n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = list()
for i in range(n):
    data.append(list(map(int, input().split())))


def turn(dir):
    if dir == 0:
        return 3
    else:
        return dir - 1


def search(row, col, dir):
    if dir == 0:
        if data[row][col - 1] == 0:
            return 0
        elif data[row][col - 1] == 1:
            return 1
        elif data[row][col - 1] == 5:
            return 5
    elif dir == 1:
        if data[row - 1][col] == 0:
            return 0
        elif data[row - 1][col] == 1:
            return 1
        elif data[row - 1][col] == 5:
            return 5
    elif dir == 2:
        if data[row][col + 1] == 0:
            return 0
        elif data[row][col + 1] == 1:
            return 1
        elif data[row][col + 1] == 5:
            return 5
    elif dir == 3:
        if data[row + 1][col] == 0:
            return 0
        elif data[row + 1][col] == 1:
            return 1
        elif data[row + 1][col] == 5:
            return 5


def clean(row, col, dir):
    if dir == 0:
        data[row - 1][col] = 5
        return row - 1, col
    elif dir == 1:
        data[row][col + 1] = 5
        return row, col + 1
    elif dir == 2:
        data[row + 1][col] = 5
        return row + 1, col
    elif dir == 3:
        data[row][col - 1] = 5
        return row, col - 1


def reverse(row, col, dir):
    if dir == 0:
        return row + 1, col
    elif dir == 1:
        return row, col - 1
    elif dir == 2:
        return row - 1, col
    elif dir == 3:
        return row, col + 1


def is_wall(row, col, dir):
    if dir == 0:
        if data[row + 1][col] == 1:
            return True
        else:
            return False
    elif dir == 1:
        if data[row][col - 1] == 1:
            return True
        else:
            return False
    elif dir == 2:
        if data[row - 1][col] == 1:
            return True
        else:
            return False
    elif dir == 3:
        if data[row][col + 1] == 1:
            return True
        else:
            return False


data[r][c] = 5
count = 1
while True:
    res = search(r, c, d)
    if res == 0:
        d = turn(d)
        r, c = clean(r, c, d)
        count += 1

    else:
        i = 0
        flag = 0
        while search(r, c, d) != 0:
            d = turn(d)
            if i == 3:
                flag = 1
                break
            i += 1
        if flag == 0:
            d = turn(d)
            r, c = clean(r, c, d)
            count += 1
        else:
            if is_wall(r, c, d):
                break
            else:
                r, c = reverse(r, c, d)

print(count)
