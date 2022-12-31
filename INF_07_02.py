n = int(input())
s_t = list()
s_p = list()
max_price = -1
for i in range(n):
    t, p = map(int, input().split())
    s_t.append(t)
    s_p.append(p)


def dfs(time, price):
    global max_price
    if time > n:
        return
    if time == n:
        if price > max_price:
            max_price = price
        return
    else:
        dfs(time + s_t[time], price + s_p[time])
        dfs(time + 1, price)


if __name__ == "__main__":
    dfs(0, 0)
    print(max_price)
