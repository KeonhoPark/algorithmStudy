n, k = map(int, input().split())
data = list(map(int, input().split()))
sum = set()

for i in range(len(data)):
    for j in range(i+1, len(data)):
        for l in range(j+1, len(data)):
            sum.add(data[i]+data[j]+data[l])

sum = list(sum)
sum.sort(reverse=True)
print(sum[k-1])

