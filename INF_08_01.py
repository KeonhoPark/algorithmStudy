n = int(input())
answer = [0] * n
answer[0] = 1
answer[1] = 2

for i in range(2, len(answer)):
    answer[i] = answer[i-1] + answer[i-2]

print(answer[n-1])

