n, m = map(int, input().split())
package = list()
one = list()
for _ in range(m):
    p, o = map(int, input().split())
    package.append(p)
    one.append(o)

min_p = min(package)
min_o = min(one)
price = [0 for _ in range(n+1)]
price[1] = min(min_p, min_o)

for i in range(2, n+1):
    price[i] = min(min_p * (i // 6) + min_o * (i % 6), min_p * ((i // 6) + 1), min_o * (i))

print(price[-1])

