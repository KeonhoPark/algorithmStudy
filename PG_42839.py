count = 0
res = list()


def dfs(l, numbers, visited, n):
    global count

    if l == len(numbers):
        return

    else:
        for i in range(len(numbers)):
            if visited[i] == 0:
                n += numbers[i]
                visited[i] = 1
                tmp = int(n)
                if tmp > 1 and tmp not in res:
                    for j in range(2, tmp):
                        if tmp % j == 0:
                            break
                    else:
                        res.append(tmp)
                        count += 1

                dfs(l + 1, numbers, visited, n)
                n = n[:len(n) - 1:]
                visited[i] = 0


def solution(numbers):
    numbers = list(numbers)
    visited = [0 for _ in range(len(numbers))]

    dfs(0, numbers, visited, '')

    return count
