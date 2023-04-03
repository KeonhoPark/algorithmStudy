import sys

sys.setrecursionlimit(10 ** 6)

count = 0


def dfs(l, numbers, total, target, visited):
    global count

    if l == len(numbers):

        if total == target:
            count += 1
        return

    else:
        if visited[l] == 0:
            visited[l] = 1
            for j in range(2):
                if j == 0:
                    total += numbers[l]
                    dfs(l + 1, numbers, total, target, visited)
                    total -= numbers[l]
                else:
                    total -= numbers[l]
                    dfs(l + 1, numbers, total, target, visited)
                    total += numbers[l]

            visited[l] = 0


def solution(numbers, target):
    visited = [0 for _ in range(len(numbers))]
    dfs(0, numbers, 0, target, visited)
    return count
