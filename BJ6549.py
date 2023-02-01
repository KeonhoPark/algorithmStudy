import sys

while True:
    data = list(map(int, sys.stdin.readline().split()))
    n = data.pop(0)
    if n == 0:
        break
    else:
        max_size = 0
        stack = []

        for i in range(n):
            min_point = i
            while stack and stack[-1][0] >= data[i]:
                h, min_point = stack.pop()
                tmp = h * (i - min_point)
                max_size = max(tmp, max_size)

            stack.append([data[i], min_point])

        for h, p in stack:
            max_size = max(max_size, h * (n-p))

        print(max_size)
