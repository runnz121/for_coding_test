def solution(genres, plays):
    answer = []
    uuid = dict()
    db = dict()
    tot = dict()

    # 곡 실행 순서로 uuid 붙임
    for i in range(len(plays)):
        if plays[i] in uuid:
            uuid[plays[i]].append(i)
        else:
            uuid[plays[i]] = [i]

    # 클래식, 팝 분류해서 곡의 실행횟수 담기
    for i in range(len(genres)):
        if genres[i] in db:
            db[genres[i]].append(plays[i])
        else:
            db[genres[i]] = [plays[i]]

    db_sort = sorted(db.items(), key=lambda x: x[1][0], reverse=True)

    # print(db)
    # print(db_sort)

    # 각 장르의 총 플레이 횟수 합 높은 순서대로 정리
    for i in db.keys():
        tot[i] = sum(db[i])
    res = sorted(tot.items(), key=lambda x: x[1], reverse=True)

    # print(res)

    for i in res:
        # print("res", i)
        for j in range(len(db_sort)):
            if i[0] == db_sort[j][0]:
                in_sort = sorted(db_sort[j][1], reverse=True)

                # for x in range(2):
                #     uuid[in_sort[x]].sort(reverse=False)
               # print(uuid)
               #  print(in_sort)
               #  print('uuid',uuid)
                answer.append(uuid[in_sort[0]][0])
                del uuid[in_sort[0]][0]


                if len(in_sort) >= 2:
                    answer.append(uuid[in_sort[1]][0])
                    del uuid[in_sort[1]][0]


    #print('answer',answer)

    return answer


genres = ["classic", "classic", "pop", "classic", "pop", "classic"]
plays = [500, 500, 600, 150,  2500, 500]
#        0     1    2    3     4     5
solution(genres, plays)
