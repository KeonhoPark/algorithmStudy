n = int(input())
time = list()

for i in range(n):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))

et = 0
count = 0

for s, e in time:
    if s >= et:
        et = e
        count += 1

print(count)
