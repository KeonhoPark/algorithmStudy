from collections import Counter


def solution(clo):
    count = 1
    clothes = dict()
    type_list = list()

    for c in clo:
        clothes[c[0]] = c[1]

    for item_type in clothes.values():
        type_list.append(item_type)

    type_list = Counter(type_list)

    for n in type_list.values():
        count *= (n + 1)

    return count - 1