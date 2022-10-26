x = int(input())
a = 1
sum = 0
bunmo = 1
bunja = 1

while sum < x:
    sum += a
    if sum < x:
        a += 1

if a % 2 == 0:
    n = sum - x
    bunmo = a - n
    bunja = 1 + n

else:
    n = sum - x
    bunmo = 1 + n
    bunja = a - n

print(bunmo, '/', bunja, sep='')