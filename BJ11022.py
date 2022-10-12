n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print('Case #%i: %i + %i = %i'%(i+1, a, b, a+b))