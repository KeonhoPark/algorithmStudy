import copy

data = list()

for i in range(7):
    data.append(list(map(int, input().split())))

def row(data):
    count = 0
    for i in range(7):
        for j in range(3):
            h = copy.deepcopy(data[i][j:j+5])
            if h == h[::-1]:
                count += 1
    return count

def col(data):
    count = 0
    for i in range(7):
        for j in range(3):
            h = list()
            for k in range(j, j+5):
                h.append(data[k][i])
            if h == h[::-1]:
                count += 1
    return count

print(row(data) + col(data))



