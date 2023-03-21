def solution(genres, plays):
    songs = dict()
    total = dict()
    res = list()

    for i in range(len(genres)):
        songs[i] = [genres[i], plays[i]]

    for song, data in songs.items():
        if data[0] in total:
            total[data[0]] += data[1]
        else:
            total[data[0]] = data[1]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    songs = sorted(songs.items(), key=lambda x: x[1][1], reverse=True)

    for t in total:
        count = 0
        for data in songs:
            if count < 2 and data[1][0] == t[0]:
                res.append(data[0])
                count += 1

    # print(songs)
    # print(total)
    # print(res)

    return res
