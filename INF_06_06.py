n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]
res = [0] * m
count = 0


def dfs(root):
    global count
    if root == m:
        for r in res:
            print(r, end=" ")
        print()
        count += 1
        return
    else:
        for d in data:
            res[root] = d
            dfs(root + 1)


if __name__ == "__main__":
    dfs(0)
    print(count)
