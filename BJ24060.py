n, k = map(int, input().split())
data = list(map(int, input().split()))
count = 0
result = -1

def merge_sort(a, p, r):
    if p < r and count <= k:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    global count, result
    tmp = list()
    i = p
    j = q + 1
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        a[i] = tmp[t]
        count += 1
        if count == k:
            result = a[i]
            break
        i += 1
        t += 1


data = merge_sort(data, 0, len(data)-1)
print(result)
