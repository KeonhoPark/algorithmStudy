# n = int(input())
# data = [0 for _ in range(n)]
# count = 0
#
#
# def dfs(l):
#     global count
#     if l == n:
#         count += 1
#         return
#     else:
#         for i in range(n):
#             data[l] = i
#             if promising(l):
#                 dfs(l + 1)
#
#
# def promising(row):
#     for i in range(row):
#         if data[row] == data[i] or abs(data[row] - data[i]) == abs(row - i):
#             return False
#
#     return True
#
#
# dfs(0)
# print(count)


n = int(input())
data = [0 for _ in range(n)]
count = 0


def dfs(l):
    global count

    if l == n:
        count += 1
        return
    else:
        flag = 0
        for i in range(n):
            data[l] = i
            if promising(l):
                if dfs(l + 1) == 1:
                    data[l] = 0
                    continue
                flag = 1
            data[l] = 0

        if flag == 0:
            return 1


def promising(row):
    for i in range(row):
        if data[row] == data[i] or abs(data[row] - data[i]) == abs(row - i):
            return False

    return True


dfs(0)
print(count)

