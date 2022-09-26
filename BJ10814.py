number = int(input())

data = []

for i in range(number):
    age, name = input().split()
    age = int(age)
    data.append([age, name])

data.sort(key = lambda x : x[0])

for n in range(number):
    print(data[n][0], data[n][1])



