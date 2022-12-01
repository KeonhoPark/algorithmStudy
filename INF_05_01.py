n, m = input().split()
data = list(n)
m = int(m)

ans = list()
ans.append(data[0])

count = 0
for i in range(1, len(data)):
    if ans[len(ans)-1] < data[i]:
        while count < m and len(ans) != 0:
            if ans[len(ans)-1] < data[i]:
                ans.pop()
                count += 1
            else:
                break
        ans.append(data[i])
    else:
        if (m - count) == (len(data) - i):
            break
        else:
            ans.append(data[i])

for i in range(len(ans)):
    print(ans[i], end="")

print()
a = list(input())
if ans == a:
    print("true")



