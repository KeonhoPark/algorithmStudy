l = int(input())
data = list(map(int, input().split()))
m = int(input())

for i in range(m):
    max = 0
    min = 101
    max_idx = -1
    min_idx = -1
    for j in range(l):
        if data[j] > max:
            max_idx = j
            max = data[j]
        if data[j] < min:
            min_idx = j
            min = data[j]

    data[max_idx] -= 1
    data[min_idx] += 1

data.sort()
print(data[l-1] - data[0])






