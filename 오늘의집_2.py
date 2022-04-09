def solution(call):
    cand = []
    idx = []

    db = dict()

    call_low = call.lower()
    call_arr = list(call_low)

    list_call = list(call)

    for i in call_low:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1

    res = sorted(db.items(), key=lambda x: x[1], reverse=True)

    maxx = res[0][1]

    for key in db.keys():
        if db[key] == maxx:
            cand.append(key)

    for k in range(len(cand)):
        for j in range(len(call_arr)):
            if cand[k] == call_arr[j]:
                call_arr[j] = ''
                idx.append(j)
    for j in idx:
        list_call[j] = ''

    answer = "".join(list_call)


    return answer


call = "ABCabcA"
solution(call)
