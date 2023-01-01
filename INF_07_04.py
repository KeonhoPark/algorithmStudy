t = int(input())
k = int(input())
c_p = list()
c_n = list()
count = 0
for i in range(k):
    p, n = map(int, input().split())
    c_p.append(p)
    c_n.append(n)


def dfs(l, total):
    global count
    if total > t:
        return
    if l == k:
        if total == t:
            count += 1
    else:
        for i in range(c_n[l] + 1):
            dfs(l + 1, total + (c_p[l] * i))


if __name__ == "__main__":
    dfs(0, 0)
    print(count)
