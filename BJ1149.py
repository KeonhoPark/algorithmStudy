n = int(input())

color = [[0 for col in range(3)] for row in range(n)]
price = [[0 for col in range(3)] for row in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    color[i][0] = r
    color[i][1] = g
    color[i][2] = b

price[0][0] = color[0][0]
price[0][1] = color[0][1]
price[0][2] = color[0][2]

for i in range(1, n):
    price[i][0] = min(price[i-1][1], price[i-1][2]) + color[i][0]
    price[i][1] = min(price[i-1][0], price[i-1][2]) + color[i][1]
    price[i][2] = min(price[i-1][0], price[i-1][1]) + color[i][2]

print(min(price[n-1]))
