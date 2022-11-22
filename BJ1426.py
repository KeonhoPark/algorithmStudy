n = int(input())-1
data = list()
data.append(666)

for i in range(667, 5000000):
    if str(i).__contains__("666"):
        data.append(i)

print(data[n])
