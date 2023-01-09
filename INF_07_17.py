n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
house = list()
pizza = list()
selected = [0] * m
res = 1e9


def dfs(l, s):
    global res

    if l == m:
        sum = 0
        for h in house:
            h_row = h[0]
            h_col = h[1]
            dis = 1e9
            for sel in selected:
                p_row = pizza[sel][0]
                p_col = pizza[sel][1]
                dis = min(dis, abs(h_row - p_row) + abs(h_col - p_col))
            sum += dis

        if res > sum:
            res = sum

    else:
        for i in range(s, len(pizza)):
            selected[l] = i
            dfs(l + 1, i + 1)


for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house.append([i, j])
        elif data[i][j] == 2:
            pizza.append([i, j])

dfs(0, 0)
print(res)
