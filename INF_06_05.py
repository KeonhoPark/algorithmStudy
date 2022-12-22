max_w, n = map(int, input().split())
data = list()

for i in range(n):
    data.append(int(input()))


def dfs(root_idx, weight, tsum):
    global res
    #total - tsum -> 전체 바둑이 무게 - 현재까지 판단한 바둑이 무게 == (남은 바둑이 무게)
    #현재까지 판단해서 더해진 무게 + 판단해야할 바둑이 무게 < 결과 이면 내려갈 필요가 없음
    if weight + (total - tsum) < res:
        return
    if root_idx > n - 1:
        if weight <= max_w:
            if res < weight:
                res = weight
        else:
            return
    else:
        if weight <= max_w:
            w = data[root_idx]
            dfs(root_idx + 1, weight, tsum + w)
            if weight + w <= max_w:
                dfs(root_idx + 1, weight + w, tsum + w)
        else:
            return


if __name__ == "__main__":
    res = -100
    total = sum(data)
    dfs(0, 0, 0)
    print(res)
