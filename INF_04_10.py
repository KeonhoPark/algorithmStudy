n = int(input())
rev = list(map(int, input().split()))
ans = [0 for i in range(n)]


for i in range(n):
    j = 0
    c = 0
    if rev[i] == c and ans[c] == 0:
        ans[c] = i+1
    else:
        while j < n:
            if ans[j] == 0:
                c += 1
                j += 1
            else:
                j += 1
            if c == rev[i]:
                if ans[j] == 0:
                    ans[j] = i+1
                    break
                else:
                    while ans[j] != 0:
                        j += 1
                    ans[j] = i+1
                    break


for i in range(len(ans)):
    print(ans[i], end=" ")

