n, u = map(int, input().split())
num = [i for i in range(1, n + 1)]
res = [0] * n
flag = [0] * (n + 1)
f = 0


def dfs(root):
    global n, f
    if root == n:
        sum_res = res.copy()
        # print(res)
        while len(sum_res) > 1:
            for j in range(len(sum_res) - 1):
                sum = sum_res[j] + sum_res[j + 1]
                sum_res[j] = sum
            sum_res.pop()
        if sum_res.pop() == u and f == 0:
            for r in res:
                print(r, end=" ")
            f = 1
        return
    else:
        for i in range(len(num)):
            if flag[i] == 0:
                flag[i] = 1
                res[root] = num[i]
                dfs(root + 1)
                flag[i] = 0


if __name__ == "__main__":
    dfs(0)
