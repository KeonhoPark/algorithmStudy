n = int(input())
con = list(map(int, input().split()))
con.sort(reverse=True)
count = 0
m = int(sum(con) / n)
s = sum(con)

for i in range(s % n):
    count += abs(con[i] - (m + 1))

for i in range(s % n, n):
    count += abs(con[i] - m)

print(int(count / 2))



