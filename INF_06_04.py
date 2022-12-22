n = int(input())
data = list(map(int, input().split()))
res = list()

def dfs(root_idx, left, right):

    if root_idx >= n:
        if left == right:
            res.append(1)
        else:
            res.append(0)

    else:
        root = data[root_idx]
        left += root
        dfs(root_idx+1, left, right)
        left -= root
        right += root
        dfs(root_idx+1, left, right)


dfs(0, 0, 0)
print(res)
if sum(res) == 0:
    print("NO")
else:
    print("YES")

