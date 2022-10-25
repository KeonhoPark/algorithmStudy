w = list(input())
data = [0 for i in range(91)]
max = 0
idx = 0
flag = 0

for i in range(len(w)):
    if w[i].islower():
        w[i] = w[i].upper()

    data[ord(w[i])] += 1

for j in range(len(data)):
    if data[j] > max:
        flag = 0
        max = data[j]
        idx = j
    elif data[j] == max:
        flag = 1

if flag == 1:
    print('?')
else:
    print(chr(idx))


