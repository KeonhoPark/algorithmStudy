n = int(input())
data = list(map(int, input().split()))
sum = list()

def digit_sum(x):
    sum = 0
    while x != 0:
        sum += (x % 10)
        x = x // 10
    return sum

for i in data:
    sum.append(digit_sum(i))

for i in range(len(sum)):
    if sum[i] == max(sum):
        print(data[i])
        break

