n = int(input())
data = []

data = list(map(int, input().split()))
new_data = sorted(set(data))
dic = {new_data[i] : i for i in range(len(new_data))}

for n in data:
    print(dic[n], end=" ")




