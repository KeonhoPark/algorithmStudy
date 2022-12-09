first = list(input())
second = list(input())
str1 = [0] * 52
str2 = [0] * 52

for f in first:
    if f.isupper():
        str1[ord(f) - 65] += 1
    else:
        str1[ord(f) - 71] += 1

for s in second:
    if s.isupper():
        str2[ord(s) - 65] += 1
    else:
        str2[ord(s) - 71] += 1

for i in range(len(str1)):
    if str1[i] != str2[i]:
        print("NO")
        break

else:
    print("YES")







