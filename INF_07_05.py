n = int(input())
coin = list()
for i in range(n):
    c = int(input())
    coin.append(c)

m = 1e9
people = [0] * 3


def dfs(l):
    global m
    if l == n:
        for j in range(len(people)-1):
            for k in range(j+1, len(people)):
                if people[j] == people[k]:
                    return
        total_min = max(people) - min(people)
        if total_min < m:
            m = total_min
        return
    else:
        for i in range(len(people)):
            people[i] += coin[l]
            dfs(l + 1)
            people[i] -= coin[l]


if __name__ == "__main__":
    dfs(0)
    print(m)
