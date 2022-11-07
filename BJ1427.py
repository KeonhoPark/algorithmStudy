n = list(input())

n = sorted(n, reverse=True)

for i in range(len(n)):
    print(n[i], end='')