data = list(input())
count = 0
stack = list()

for i in range(len(data)):
    if data[i] == '(':
        stack.append(data[i])
    else:
        stack.pop()
        if data[i-1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)

