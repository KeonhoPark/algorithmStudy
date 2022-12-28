n, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
m = int(input())
count = 0
res = [0 for i in range(k)]
flag = dict()
for x in data:
    flag[x] = 0


def dfs(root):
    global count
    if root == k:
        if sum(res) < m:
            return
        else:
            for i in range(len(res)-1):
                if res[i] > res[i + 1]:
                    break
            else:
                if sum(res) % m == 0 and res[i] < res[i+1]:
                    count += 1
            return
    else:
        for d in data:
            if flag[d] == 0:
                flag[d] = 1
                res[root] = d
                dfs(root + 1)
                flag[d] = 0


if __name__ == "__main__":
    dfs(0)
    print(count)
