import sys
from collections import deque

data = list(sys.stdin.readline().strip())
data = deque(data)
word = list(sys.stdin.readline().strip())
count = 0

i = 0
while i < len(data) and len(word) <= len(data):
    flag = 0
    for k in range(len(word)):
        if (i + k < len(data) and data[i + k] != word[k]) or (i + k == len(data) - 1 and k < len(word) - 1):
            i += 1
            flag = 1
            break


    if flag == 0:
        for t in range(i + len(word)):
            if data:
                data.popleft()
        count += 1
        i = 0

print(data)
print(count)
