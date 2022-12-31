n = int(input())
weight = list(map(int, input().split()))
res = [0 for i in range(sum(weight) + 1)]


def dfs(l, total):
    if l == n:
        if total > 0:
            res[total] = 1
        return
    else:
        dfs(l + 1, total + weight[l])
        dfs(l + 1, total - weight[l])
        dfs(l + 1, total)


if __name__ == "__main__":
    dfs(0, 0)
    count = 0
    for i in range(1, len(res)):
        if res[i] == 0:
            count += 1
    print(count)
