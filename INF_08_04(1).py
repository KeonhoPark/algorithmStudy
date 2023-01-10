n = int(input())
data = [0] * (n+1)


def dfs(n):
    if n == 1 or n == 2:
        data[n] = n+1
        return n+1

    if data[n] != 0:
        return data[n]

    else:
        data[n] = dfs(n-1) + dfs(n-2)
        return dfs(n-1) + dfs(n-2)


print(dfs(n))



