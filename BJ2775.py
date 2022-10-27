t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    f0 = [i for i in range(1, n+1)]

    for j in range(k):
        for l in range(1, n):
            f0[l] += f0[l-1]
    print(f0[-1])
