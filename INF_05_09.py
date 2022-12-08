first = list(input())
second = list(input())

for i in range(len(first)):
    for j in range(len(second)):
        if first[i] == second[j]:
            second.pop(j)
            break

if len(second) == 0:
    print("YES")
else:
    print("NO")
