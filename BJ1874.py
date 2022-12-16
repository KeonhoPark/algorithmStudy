import sys

n = int(input())
data = list()
res = list()

for _ in range(n):
    data.append(int(input()))

i = 1
stack = list()
stack.append(i)
res.append('+')
flag = 0
for d in data:
    if d == i:
        stack.pop()
        res.append('-')
    elif i < d:
        while i < d:
            stack.append(i+1)
            res.append('+')
            i += 1
        stack.pop()
        res.append('-')
    else:
        if len(stack) != 0:
            while d < stack[-1]:
                stack.pop()
                res.append('-')
            stack.pop()
            res.append('-')
        else:
            print("NO")
            flag = 1
            break

if flag != 1:
    for r in res:
        print(r)













