import sys

while True:
    string = list(sys.stdin.readline())
    string.pop()
    if string == ['.']:
        break
    else:
        stack = list()
        flag = 0

        for s in string:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if len(stack) != 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        break
                else:
                    flag = 1
                    break

            elif s == ']':
                if len(stack) != 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        break
                else:
                    flag = 1
                    break

        if len(stack) == 0 and flag == 0:
            print("yes")
        else:
            print("no")














