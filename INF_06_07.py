n = int(input())
coin = list(map(int, input().split()))
coin = sorted(coin, reverse=True)
m = int(input())
res = 100000


def dfs(root, sum):
    global res
    if sum > m:
        return
    if root > res:
        return
    if sum == m:
        if root < res:
            res = root
    else:
        for c in coin:
            dfs(root + 1, sum + c)



dfs(0, 0)
print(res)
