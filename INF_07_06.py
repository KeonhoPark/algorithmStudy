alp = list(map(int, input()))
res = [0 for i in range(len(alp))]
count = 0


def dfs(l, res_pos):
    global count, n
    if l == n:
        for r in res:
            if r != 0:
                print(chr(r + 64), end="")
        print()
        count += 1
        return
    else:
        for i in range(1, 27):
            if alp[l] == i:
                res[res_pos] = i
                dfs(l + 1, res_pos + 1)
                res[res_pos] = 0
            elif i >= 10 and (alp[l] * 10) + alp[l+1] == i:
                res[res_pos] = i
                dfs(l + 2, res_pos + 1)
                res[res_pos] = 0


if __name__ == "__main__":
    n = len(alp)
    alp.append(-100)
    dfs(0, 0)
    print(count)
