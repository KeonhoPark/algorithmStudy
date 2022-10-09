n = int((input()))
data = list(map(int, input().split()))

ans = [1 for num in range(n)]

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j] and ans[i] <= ans[j]:
            ans[i] = ans[j] + 1

print(max(ans))



