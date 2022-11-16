k = int(input())
count = 0

def hanoi(k, start, end):
    if k == 1:
        print(start, end)
        return

    hanoi(k-1, start, 6-start-end)
    print(start, end)
    hanoi(k-1, 6-start-end, end)


hanoi(k, 1, 3)