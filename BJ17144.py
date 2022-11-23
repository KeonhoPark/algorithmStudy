import copy

r, c, t = map(int, input().split())
data = []
cleaner = 0

for i in range(r):
    data.append(list(map(int, input().split())))

for k in range(t):
    dust = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if data[i][j] != 0 and data[i][j] != -1:
                count = 0
                if j-1 >= 0 and data[i][j-1] != -1:
                    dust[i][j-1] += data[i][j] // 5
                    count += 1
                if j+1 < c and data[i][j+1] != -1:
                    dust[i][j+1] += data[i][j] // 5
                    count += 1
                if i-1 >= 0 and data[i-1][j] != -1:
                    dust[i-1][j] += data[i][j] // 5
                    count += 1
                if i+1 < r and data[i+1][j] != -1:
                    dust[i+1][j] += data[i][j] // 5
                    count += 1
                data[i][j] = data[i][j] - ((data[i][j] // 5) * count)
            elif data[i][j] == -1:
                uc = i-1
                lc = i

    for i in range(r):
        for j in range(c):
            data[i][j] = data[i][j] + dust[i][j]

    temp = copy.deepcopy(data)

    #uc
    for i in range(1, c):
        data[uc][1] = 0
        if i + 1 > c-1:
            break
        data[uc][i+1] = temp[uc][i]

    for i in range(uc, -1, -1):
        if i-1 < 0:
            break
        data[i-1][c-1] = temp[i][c-1]

    for i in range(c-1, -1, -1):
        if i-1 < 0:
            break
        data[0][i-1] = temp[0][i]

    for i in range(uc):
        if i+1 == uc:
            continue
        data[i+1][0] = temp[i][0]

    #lc
    for i in range(1, c):
        data[lc][1] = 0
        if i + 1 > c-1:
            break
        data[lc][i+1] = temp[lc][i]

    for i in range(lc, r-1):
        if i + 1 > r:
            break
        data[i + 1][c-1] = temp[i][c-1]

    for i in range(c-1, -1, -1):
        if i-1 < 0:
            break
        data[r-1][i-1] = temp[r-1][i]

    for i in range(r-1, lc, -1):
        if i-1 == lc:
            continue
        data[i-1][0] = temp[i][0]


s = 0
for i in range(r):
    #print(data[i])
    s += sum(data[i])

print(s+2)



