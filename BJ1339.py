import copy
from collections import deque


def set_score(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            score[ord(data[i][j])] += (1 * (10 ** (len(data[i]) - j - 1)))


n = int(input())
data = [deque(input()) for _ in range(n)]
score = [0 for _ in range(ord('Z') + 1)]
set_score(data)

q = deque(copy.deepcopy(data))
res = [0 for _ in range(ord('Z') + 1)]

idx = 9
sum = 0

while max(score) != 0:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if score[ord(data[i][j])] == max(score):
                res[ord(data[i][j])] = idx
    idx -= 1
    score[score.index(max(score))] = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = res[ord(data[i][j])]
        sum += data[i][j] * (10 ** (len(data[i]) - j - 1))

print(sum)
