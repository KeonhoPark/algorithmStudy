t = int(input())

for i in range(t):
    data = ''
    r, s = input().split()
    r = int(r)
    s = list(s)
    for j in range(len(s)):
        data = data + s[j]*r
    print(data)