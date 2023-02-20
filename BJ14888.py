import copy

n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))
oper_n = sum(oper)
mx = -1e9
mn = 1e9
res = data[0]


def dfs(l):
    global mx, mn, res
    if l == oper_n:
        mn = min(mn, res)
        mx = max(mx, res)
        return
    else:
        tmp = copy.deepcopy(res)
        for i in range(len(oper)):
            if oper[i] != 0:
                oper[i] -= 1
                if i == 0:
                    res += data[l + 1]
                    dfs(l + 1)
                    res = tmp
                    oper[i] += 1
                elif i == 1:
                    res -= data[l + 1]
                    dfs(l + 1)
                    res = tmp
                    oper[i] += 1
                elif i == 2:
                    res *= data[l + 1]
                    dfs(l + 1)
                    res = tmp
                    oper[i] += 1
                else:
                    if res < 0 and data[l + 1] > 0:
                        res = res * (-1)
                        x = res // data[l + 1]
                        res = x * (-1)
                    else:
                        res //= data[l + 1]
                    dfs(l + 1)
                    res = tmp
                    oper[i] += 1


dfs(0)
print(mx)
print(mn)
