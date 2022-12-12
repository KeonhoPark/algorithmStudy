import sys

n = int(input())

for i in range(n):
    data = list(input())
    stack = list()
    flag = 0

    for d in data:
        if d == '(':
            stack.append(d)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                flag = 1
                break

    if len(stack) == 0 and flag == 0:
        print("YES")

    else :
        print("NO")





