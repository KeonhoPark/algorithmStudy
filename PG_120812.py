from collections import Counter

def solution(array):
    array = Counter(array)
    array = dict(sorted(array.items(), reverse=True, key=lambda x: x[1]))
    keys = list(array.keys())
    if len(keys) == 1:
        return keys[0]
    elif array[keys[0]] == array[keys[1]]:
        return -1
    return keys[0]
