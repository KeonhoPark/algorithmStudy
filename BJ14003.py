import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
MAX = sys.maxsize
res_count = [-MAX]
res_list = [(-MAX, -1)]


def bin_srch(x):
    s = 0
    e = len(res_count) - 1

    while s <= e:
        mid = (s + e) // 2
        if x == res_count[mid]:
            return mid
        elif x > res_count[mid]:
            s = mid + 1
        else:
            e = mid - 1

    return s


for i in range(len(data)):
    if data[i] > res_count[-1]:
        res_count.append(data[i])
        res_list.append((data[i], len(res_count) - 1))
    else:
        idx = bin_srch(data[i])
        res_count[idx] = data[i]
        res_list.append((data[i], idx))

print(len(res_count) - 1)
# print(res_count)
# print(res_list)

answer = list()
tmp = len(res_count) - 1
flag = 0

for i in range(len(res_list) - 1, 0, -1):
    if tmp == res_list[i][1] and flag == 0:
        flag = 1
        answer.append(res_list[i][0])

    elif res_list[i][1] == tmp - 1 and flag == 1:
        tmp = res_list[i][1]
        answer.append(res_list[i][0])

print(*answer[::-1])
