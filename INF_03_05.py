n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
start = 0
end = 0
while start < n and end < n:
    if sum(data[start: end+1]) < m:
        end += 1
    elif sum(data[start: end+1]) > m:
        start += 1
    else:
        count += 1
        end += 1

print(count)