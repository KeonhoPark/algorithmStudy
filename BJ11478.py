import sys

s = sys.stdin.readline().strip()
res = dict()

for i in range(1, len(s) + 1):
    for j in range(len(s) - i + 1):
        tmp = s[j:j + i:]
        if tmp not in res.keys():
            res[tmp] = 1

print(len(res))
