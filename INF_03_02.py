data = list(input())
num_list = list()
num = 0


for i in range(len(data)):
    if ord("0") <= ord(data[i]) <= ord("9"):
        num_list.append(int(data[i]))

for i in range(len(num_list)):
    num += num_list[i] * (10 ** (len(num_list) - 1 - i))

count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1

print(num)
print(count)