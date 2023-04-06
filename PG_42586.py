def solution(progresses, speeds):
    r_day = list()
    res = list()

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            r_day.append((100 - progresses[i]) // speeds[i])
        else:
            r_day.append((100 - progresses[i]) // speeds[i] + 1)

    MAX = r_day[0]
    count = 0
    for day in r_day:
        if day > MAX:
            MAX = day
            res.append(count)
            count = 1
        else:
            count += 1

    res.append(count)

    return res
