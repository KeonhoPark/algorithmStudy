def solution(n):
    def contains_three(i):
        while i > 0:
            if i % 10 == 3:
                return True
            i //= 10

        return False

    count = 0
    i = 1
    while True:
        if not (i % 3 == 0 or contains_three(i)) and i - count == n:
            return i

        elif i % 3 == 0 or contains_three(i):
            count += 1

        i += 1
