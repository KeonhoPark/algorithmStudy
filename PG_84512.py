import sys
sys.setrecursionlimit(10 ** 6)

vowels = ['A', 'E', 'I', 'O', 'U']
dictionary = list()


def dfs(l, cur_word):
    if l == 5:
        return

    else:
        for i in range(len(vowels)):
            dictionary.append(cur_word + vowels[i])
            dfs(l + 1, cur_word + vowels[i])


def solution(word):
    dfs(0, '')
    return dictionary.index(word) + 1
