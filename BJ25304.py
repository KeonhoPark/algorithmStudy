total = int(input())
n = int(input())

for i in range(n):
    p, q = map(int, input().split())
    total -= (p*q)

if total == 0:
    print('Yes')
else:
    print('No')