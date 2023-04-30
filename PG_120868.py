def solution(sides):
    count = 0
    sides.sort()
    total = sum(sides)

    for i in range(1, total):
        if i + sides[0] > sides[1] and i < total:
            count += 1

    return count
