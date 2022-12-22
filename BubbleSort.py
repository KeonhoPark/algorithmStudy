def bs_asc(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]



if __name__=="__main__":
    data = list(map(int, input().split()))
    bs_asc(data)
    print(data)


