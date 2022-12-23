n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]
res = [0] * m

count = 0


def dfs(root):
    global count
    if root == m:
        count += 1
        for r in res:
            print(r, end=" ")
        print()
    else:
        for d in data:
            res[root] = d
            dfs(root+1)


dfs(0)
print(count)


