def dfs(x):
    if x == n + 1:
        for i in range(1, n + 1):
            if option[i] == 1:
                print(i, end=" ")
        print()

    else:
        option[x] = 1
        dfs(x + 1)
        option[x] = 0
        dfs(x + 1)


if __name__ == "__main__":
    n = int(input())
    option = [0] * (n + 1)
    dfs(1)
