data = [0] * 9
for i in range(9):
    data[i] = list(map(int, input().split()))


def row(data):
    for i in range(9):
        r = list()
        for j in range(9):
            r.append(data[i][j])

        r.sort()
        for k in range(len(r)):
            if r[k] != k+1:
                return False
    return True

def col(data):
    for i in range(9):
        c = list()
        for j in range(9):
            c.append(data[j][i])

        c.sort()
        for k in range(len(c)):
            if c[k] != k+1:
                return False
    return True


def square(data):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            s = list()
            for m in range(i, i+3):
                for n in range(j, j+3):
                    s.append(data[m][n])

            s.sort()
            for k in range(len(s)):
                if s[k] != k+1:
                    return False
    return True

if row(data) and col(data) and square(data):
    print("YES")
else:
    print("NO")



