import sys
from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    res[s] = 1
    while q:
        p = q.popleft()
        for nb in data[p]:
            if visited[nb] == 0:
                visited[nb] = 1
                res[nb] = res[p] * (-1)
                q.append(nb)


def check(res):
    for i in range(1, len(data)):
        for n in data[i]:
            if res[i] == res[n]:
                return False

    return True


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, e = map(int, sys.stdin.readline().split())
        data = [[] for _ in range(n + 1)]

        for i in range(e):
            start, end = map(int, sys.stdin.readline().split())
            data[start].append(end)
            data[end].append(start)

        visited = [0 for _ in range(n + 1)]
        res = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if visited[i] == 0:
                bfs(i)
        if not check(res):
            print("NO")

        else:
            print("YES")


