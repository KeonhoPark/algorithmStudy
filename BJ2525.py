h, m = map(int, input().split())
time = int(input())

if m + time >= 60:
    h += (m + time) // 60
    h = h % 24
    m = (m + time) % 60

else:
    m += time

print(h, m)



