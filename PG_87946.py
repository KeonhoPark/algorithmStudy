mx = -1
count = 0


def dfs(l, ds, visited, k):
    global count, mx

    if l == len(ds):
        return

    else:
        for i in range(len(ds)):
            if visited[i] == 0 and k >= ds[i][0]:
                visited[i] = 1
                count += 1
                if count > mx:
                    mx = count
                dfs(l + 1, ds, visited, k - ds[i][1])
                visited[i] = 0
                count -= 1


def solution(k, ds):
    visited = [0 for _ in range(len(ds))]
    dfs(0, ds, visited, k)
    return mx
