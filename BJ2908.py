a, b = input().split()
a = list(map(int, a))
b = list(map(int, b))
new_a = a[2]*100 + a[1]*10 + a[0]
new_b = b[2]*100 + b[1]*10 + b[0]

if new_a > new_b:
    print(new_a)
else:
    print(new_b)

