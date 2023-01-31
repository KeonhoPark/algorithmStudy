a, b, c = map(int, input().split())


def dfs(a, b):
    if b == 1:
        return a % c
    else:
        r = dfs(a, b // 2)
        if b % 2 == 0:
            return (r ** 2) % c
        else:
            return (r ** 2 * a) % c


print(dfs(a, b))
