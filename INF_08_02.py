n = int(input())
data = [0] * (n + 1)


def dfs(l):
    if l == 1 or l == 2:
        return l
    if data[l] != 0:
        return data[l]
    else:
        data[l] = dfs(l-1) + dfs(l-2)
        return data[l]


print(dfs(n))




