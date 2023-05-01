from itertools import permutations


def solution(babbling):
    count = 0
    p = ["aya", "ye", "woo", "ma"]
    dictionary = list()

    for i in range(1, 5):
        for words in permutations(p, i):
            tmp = ''
            for word in words:
                tmp += word
            dictionary.append(tmp)

    for b in babbling:
        if b in dictionary:
            count += 1

    return count

