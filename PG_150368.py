import sys

sys.setrecursionlimit(10 ** 6)


def solution(users, emoticons):
    sales_rate = [10, 20, 30, 40]
    sale_price_per_item = [[] for _ in range(len(emoticons))]
    visited = [[0 for _ in range(4)] for _ in range(len(emoticons))]
    plus_benefit = []
    combination = []

    for i in range(len(emoticons)):
        for sr in sales_rate:
            sale_price_per_item[i].append([int(emoticons[i] - (emoticons[i] * (sr / 100))), sr])

    def get_available_price(l):
        if l == len(emoticons):
            count = 0
            benefit = 0
            for u in users:
                user_rate = u[0]
                user_total = u[1]
                total = 0
                for pr in combination:
                    sale_price = pr[0]
                    sale_rate = pr[1]

                    if sale_rate >= user_rate:
                        total += sale_price

                if total >= user_total:
                    count += 1
                else:
                    benefit += total

            plus_benefit.append([count, benefit])
            return

        else:
            for i in range(len(sale_price_per_item[l])):
                if visited[l][i] == 0:
                    visited[l][i] = 1
                    combination.append(sale_price_per_item[l][i])
                    get_available_price(l + 1)
                    visited[l][i] = 0
                    combination.remove(sale_price_per_item[l][i])

    get_available_price(0)
    plus_benefit.sort(reverse=True)
    return plus_benefit[0]
