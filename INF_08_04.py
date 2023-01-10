n = int(input())

answer = [0] * (n+1)
answer[1] = 2
answer[2] = 3

for i in range(3, n+1):
    answer[i] = answer[i-1] + answer[i-2]

print(answer[n])



