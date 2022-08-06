def solution(invitationPairs):
    answer = []

    returns = []

    db = dict()

    for i in invitationPairs:
        if i[0] in db:
            db[i[0]].append(i[1])
        else:
            db[i[0]] = [i[1]]

    for i in db:
        tot = 0
        tot += len(db[i]) * 10
        for j in db[i]:
            if j in db:
                tot += len(db[j]) * 3
                for x in db[j]:
                    if x in db:
                        tot += len(db[x])
        answer.append([i, tot])


    answer.sort(key = lambda x:(x[1], -x[0]), reverse=True)

    for i in range(len(answer)):
        returns.append(answer[i][0])
        if i >= 2:
            break

    return returns

solution([[1, 2], [2, 3], [2, 4], [2, 5], [5, 6], [5, 7], [6, 8], [2, 9]])