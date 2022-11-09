import copy

n = int(input())
score = list(map(int, input().split()))
new_score = copy.deepcopy(score)

for i in range(1, len(score)):
    if score[i] == score[i-1] == 1:
        new_score[i] += new_score[i-1]

print(sum(new_score))