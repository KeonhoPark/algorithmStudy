def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    res = 0

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for c in costs:
        start, end, cost = c[0], c[1], c[2]

        if find_parent(parent, start) != find_parent(parent, end):
            union_parent(parent, start, end)
            res += cost

    return res
