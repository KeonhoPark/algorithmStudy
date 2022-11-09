n = int(input())
data = list(map(int, input().split()))

def reverse(c):
    new_num = 0
    for i in range(len(str(c))-1, -1, -1):
        new_num += (c % 10) * (10 ** i)
        c = c // 10
    return new_num

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

for i in data:
    rev = reverse(i)
    if isPrime(rev):
        print(rev, end=" ")
