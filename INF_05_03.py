data = list(input())
stack = list()


for i in range(len(data)):
    if data[i].isdecimal():
        print(data[i], end="")
    else:
        if data[i] == '(':
            stack.append(data[i])

        elif data[i] == '*' or data[i] == '/':
            while len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end="")
            stack.append(data[i])

        elif data[i] == '+' or data[i] == '-':
            while len(stack) != 0 and stack[-1] != '(':
                print(stack.pop(), end="")
            stack.append(data[i])

        elif data[i] == ')':
            while len(stack) != 0 and stack[-1] != '(':
                print(stack.pop(), end="")
            stack.pop()


for i in range(len(stack)):
    print(stack.pop(), end="")