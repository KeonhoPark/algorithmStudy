n = int(input())
coin = list(map(int, input().split()))
m = int(input())
coin.sort(reverse=True)
result = 1e9


def dfs(root, sum):
    global result
    if root > result:
        return
    if sum > m:
        return
    if sum == m:
        result = root
    else:
        for c in coin:
            dfs(root+1, sum+c)


if __name__=="__main__":
    dfs(0, 0)
    print(result)
