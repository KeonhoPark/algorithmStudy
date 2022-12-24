n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
res = [0] * m
count = 0
flag = [0 for i in range(n+1)]


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
            if flag[d] == 0:
                flag[d] = 1
                res[root] = d
                dfs(root+1)
                flag[d] = 0




if __name__=="__main__":
    dfs(0)
    print(count)
