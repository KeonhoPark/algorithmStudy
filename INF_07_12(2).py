n = int(input())
house = [list(map(int, input())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
danji = 0
count_list = list()
count = 0


def cluster(x, y):
    global count
    neighbor = list()
    house[x][y] = 0
    count += 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n:
            neighbor.append(house[new_x][new_y])
    if sum(neighbor) == 0:
        return

    else:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                if house[new_x][new_y] == 1:
                    cluster(new_x, new_y)


for i in range(n):
    for j in range(n):
        if house[i][j] == 1:
            cluster(i, j)
            count_list.append(count)
            count = 0
            danji += 1

print(danji)
count_list.sort()
print(*count_list, sep="\n")
