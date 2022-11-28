n = int(input())
players = list()

for i in range(n):
    players.append(list(map(int, input().split())))

players.sort(reverse=True)
print(players)
print()

count = 0
max = 0
for h, w in players:
    if w > max:
        max = w
        count += 1

print(count)



