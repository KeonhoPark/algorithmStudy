n = int(input())
data = list(map(int, input().split()))
answer = list()

i = 0
j = n-1
last = 0
while i <= j:
    if i == j and data[i] > last:
        answer.append("L")
        break
    elif i == j and data[i] <= last:
        break
    else:
        if data[i] < data[j]:
            if data[i] > last:
                answer.append("L")
                last = data[i]
                i += 1
            elif data[j] > last:
                answer.append("R")
                last = data[j]
                j -= 1
            else:
                break
        elif data[i] > data[j]:
            if data[j] > last:
                answer.append("R")
                last = data[j]
                j -= 1
            elif data[i] > last:
                answer.append("L")
                last = data[i]
                i += 1
            else:
                break

print(len(answer))
for i in range(len(answer)):
    print(answer[i], end="")








