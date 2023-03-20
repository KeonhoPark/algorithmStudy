from collections import Counter


def solution(phone_book):
    phone_book = Counter(phone_book)

    for a in phone_book.keys():
        for b in range(len(a)):
            # print(a)
            # print(b[:len(a):])
            if a[:b:] in phone_book:
                return False

    return True