n = int(input())
score = list(map(int, input().split()))
avg = round(sum(score) / n)
min = float('inf')
min_idx = 0
for i in range(n):
    if min > abs(score[i]-avg):
        min = abs(score[i]-avg)
        min_idx = i
    elif min == abs(score[i]-avg):
        if score[i] > score[min_idx]:
            min = abs(score[i] - avg)
            min_idx = i

print(avg, min_idx+1, end=" ")
