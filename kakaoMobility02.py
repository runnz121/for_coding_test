def solution(id_list, k):
    answer = 0

    db = dict()

    for i in id_list:
        tmp = set(i.split())
        tmp = list(tmp)
        for custom in tmp:
            if custom in db:
                if db[custom] < k:
                    db[custom] += 1
            else:
                db[custom] = 1
    for key, val in db.items():
        answer += val

    return answer

id_list = ["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"]
solution(id_list, 3)