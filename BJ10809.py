c = list(input())
data = [-1 for i in range(26)]

for i in range(len(c)):
    if data[ord(c[i]) - 97] == -1:
        data[ord(c[i]) - 97] = i

for i in range(len(data)):
    print(data[i], end=' ')

