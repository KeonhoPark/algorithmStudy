from collections import deque

m = list(input())
n = int(input())
plan = [0 for i in range(n)]

for i in range(n):
    plan[i] = (list(input()))
    plan[i] = deque(plan[i])


for i in range(n):
    must = deque(m)
    flag = 0
    while len(plan[i]) != 0:
        if len(must) == 0:
            break

        if plan[i][0] == must[0]:
            plan[i].popleft()
            must.popleft()

        else:
            for j in range(len(must)):
                if must[j] == plan[i][0]:
                    flag = 1
                    break

            if flag == 0:
                plan[i].popleft()
            else:
                break

    if len(must) != 0:
        print("#", i, " NO", sep="")
    else:
        print("#", i, " YES", sep="")
