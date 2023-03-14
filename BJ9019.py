import sys
from collections import deque


def D(n):
    res = 2 * n
    if res > 9999:
        return res % 10000

    return res


def S(n):
    if n == 0:
        return 9999
    else:
        return n - 1


def L(n):
    if n >= 1000:
        tmp_div = n // 1000
        tmp_mod = n % 1000
        return 10 * tmp_mod + tmp_div
    else:
        return 10 * n


def R(n):
    tmp_div = n // 10
    tmp_mod = n % 10
    return 1000 * tmp_mod + tmp_div


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b = map(int, sys.stdin.readline().split())

        pq = deque()
        pq.append([a, ''])

        visited = [-1 for _ in range(10000)]
        visited[a] = 0

        while pq:
            cur_n, order = pq.popleft()
            if cur_n == b:
                print(order)
                break

            else:
                next_n = -1
                o = ''
                for i in range(4):
                    if i == 0:
                        next_n = D(cur_n)
                        o = 'D'
                    elif i == 1:
                        next_n = S(cur_n)
                        o = 'S'
                    elif i == 2:
                        next_n = L(cur_n)
                        o = 'L'
                    elif i == 3:
                        next_n = R(cur_n)
                        o = 'R'

                    if not (0 <= next_n < 10000):
                        continue
                    if visited[next_n] != -1:
                        continue

                    pq.append([next_n, order + o])
                    visited[next_n] = 0
