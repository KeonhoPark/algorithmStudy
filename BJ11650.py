n = int(input())
cor = [[0, 0] for i in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    cor[i][0] = x
    cor[i][1] = y

cor.sort()
for j in range(len(cor)):
    print(cor[j][0], cor[j][1], end=" ")
    print()
