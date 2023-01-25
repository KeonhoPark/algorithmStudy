n, k = map(int, input().split())
w = list()
v = list()
for i in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

dp = [0] * (k+1)

for i in range(len(w)):
    for j in range(len(dp)-1, -1, -1):
        if j - w[i] >= 0:
            dp[j] = max(dp[j], v[i] + dp[j - w[i]])

print(dp)
print(max(dp))

