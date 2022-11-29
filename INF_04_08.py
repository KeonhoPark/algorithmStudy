n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort(reverse=True)

i = 0
j = n - 1
count = 0
while i <= j:
    if i == j:
        count += 1
        break
    else:
        if weight[i] + weight[j] > m:
            count += 1
            i += 1
        else:
            count += 1
            i += 1
            j -= 1

print(count)