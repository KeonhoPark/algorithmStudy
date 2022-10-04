n = int(input())

stair = [0 for i in range(301)]
ans = [0 for i in range(301)]

for i in range(n):
    stair[i] = int(input())

ans[0] = stair[0]
ans[1] = stair[0] + stair[1]
ans[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for j in range(3, n):
    ans[j] = max(stair[j-1] + stair[j] + ans[j-3], ans[j-2] + stair[j])

print(ans[n-1])





