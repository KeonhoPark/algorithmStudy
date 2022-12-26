n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]
count = 0
flag = [0 for i in range(n + 1)]
result = [0 for i in range(m)]


def dfs(root):
    global count
    if root == m:
        for i in range(len(result)-1):
            if result[i] >= result[i+1]:
                break
        else:
            for r in result:
                print(r, end=" ")
            print()
            count += 1
            return
        return
    else:
        for d in data:
            if flag[d] == 0:
                flag[d] = 1
                result[root] = d
                dfs(root + 1)
                flag[d] = 0


if __name__ == "__main__":
    dfs(0)
    print(count)