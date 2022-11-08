t = int(input())
for i in range(t):
    data = []
    n, s, e, k = map(int, input().split())
    data = (list(map(int, input().split())))
    new_data = []
    for j in range(s-1, e):
        new_data.append(data[j])
    new_data.sort()
    print("#%d"%(i+1),new_data[k-1])
