n = int(input())
data = list()

if n == 1:
    print()
else:
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                data.append(i)
                break

for i in range(len(data)):
    print(data[i])
