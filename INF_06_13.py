n, m = map(int, input().split())
matrix = [[0 for i in range(n)] for j in range(n)]
visited = [0 for i in range(n)]
count = 0
for i in range(n):
    matrix[i][i] = 1

for i in range(m):
    s, e = map(int, input().split())
    matrix[s-1][e-1] = 1


def dfs(root):
    global count
    visited[root] = 1
    if root == n-1:
        count += 1
        return
    else:
        for i in range(n):
            if visited[i] == 0 and matrix[root][i] == 1:
                dfs(i)
                visited[i] = 0


dfs(0)
print(count)




