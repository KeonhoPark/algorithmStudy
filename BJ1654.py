import sys

k, n = map(int, sys.stdin.readline().split())
wire = list()
for _ in range(k):
    wire.append(int(sys.stdin.readline()))

max_len = max(wire)

s = 1
e = max_len

while s <= e:
    count = 0
    mid = (s + e) // 2
    for w in wire:
        count += (w // mid)

    if count >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)

