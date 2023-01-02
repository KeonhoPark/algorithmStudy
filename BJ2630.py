n = int(input())
paper = [[0]] * n
blue = 0
white = 0
for k in range(n):
    paper[k] = list(map(int, input().split()))


def cut(row, col, l):
    global blue, white
    c = paper[col][row]
    for i in range(col, col + l):
        for j in range(row, row + l):
            if c != paper[i][j]:
                cut(row, col, l // 2)
                cut(row + l // 2, col, l // 2)
                cut(row, col + l // 2, l // 2)
                cut(row + l // 2, col + l // 2, l // 2)
                return
    if c == 1:
        blue += 1
        return
    if c == 0:
        white += 1
        return


cut(0, 0, n)
print(white)
print(blue)
