n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
m = int(input())
count = 0
res = [0 for i in range(k)]
flag = dict()
for x in data:
    flag[x] = 0


def dfs(root, parent):
    global count
    if root == k:
        if sum(res) % m != 0:
            return
        else:
            count += 1
            return
    else:
        for d in data:
            if flag[d] == 0 and d > parent:
                flag[d] = 1
                res[root] = d
                dfs(root + 1, d)
                flag[d] = 0


if __name__ == "__main__":
    dfs(0, 0)
    print(count)
