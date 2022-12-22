data = list(map(int, input().split()))


def selection_sort_asc(l):
    for i in range(len(l)-1):
        min = 99999
        for j in range(i, len(l)):
            if min > l[j]:
                min = l[j]
        min, l[i] = l[i], min


if __name__ == "__main__":
    selection_sort_asc(data)
    print(data)
