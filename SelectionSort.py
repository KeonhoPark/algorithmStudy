data = list(map(int, input().split()))


def selection_sort_asc(l):
    for i in range(len(l)-1):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[min_idx], l[i] = l[i], l[min_idx]


if __name__ == "__main__":
    selection_sort_asc(data)
    print(data)
