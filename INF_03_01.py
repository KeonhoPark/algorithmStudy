n = int(input())

for i in range(n):
    inp = input().lower()
    word = list(inp)
    j = 0
    k = len(word) - 1
    flag = 0
    while j <= k:
        if word[j] != word[k]:
            print("#%d NO" %(i+1))
            flag = 1
            break
        j += 1
        k -= 1
    if flag == 0:
        print("#%d YES" %(i+1))
