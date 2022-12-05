data = list(input())


def data_oper(i, d):
    data.pop(i)
    data.pop(i - 1)
    data.pop(i - 2)
    data.insert(i - 2, d)


while len(data) > 1:
    for i in range(len(data)):
        if data[i] == '+':
            d = int(data[i - 2]) + int(data[i - 1])
            data_oper(i, d)
            break

        elif data[i] == '-':
            d = int(data[i - 2]) - int(data[i - 1])
            data_oper(i, d)
            break

        elif data[i] == '*':
            d = int(data[i - 2]) * int(data[i - 1])
            data_oper(i, d)
            break

        elif data[i] == '/':
            d = int(data[i - 2]) / int(data[i - 1])
            data_oper(i, d)
            break

        else:
            continue

print(data[0])
