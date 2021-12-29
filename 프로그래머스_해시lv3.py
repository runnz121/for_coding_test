def solution(genres, plays):
    answer = []
    db = dict()

    for p1 in zip(genres, plays):
        song, cnt = p1[0], p1[1]

        if song in db:
            db[song].append(cnt)
        else:
            db[song] = [cnt]
        db[song].reverse()
    print(db.get(song))

    return answer