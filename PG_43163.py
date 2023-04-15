from collections import deque


def solution(begin, target, words):
    def find_one(word, words):
        word_list = list()

        for w in words:
            count = 0
            for i in range(len(w)):
                if word[i] != w[i]:
                    count += 1

            if count == 1:
                word_list.append(w)

        return word_list

    def sort_by_one(begin, words):
        one_words = find_one(begin, words)

        for w in one_words:
            words.remove(w)
            words.appendleft(w)

    if target not in words:
        return 0

    else:
        count = 0
        words = deque(words)
        sort_by_one(begin, words)

        while words:
            word = words.popleft()
            count += 1
            if word == target:
                return count

            sort_by_one(word, words)

        return 0
