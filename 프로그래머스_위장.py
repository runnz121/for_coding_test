def solution(clothes):
    answer = 1
    db = dict()

    for ele in clothes:
        cat = ele[1]
        name = ele[0]

        if cat in db:
            db[cat].append(name)
        else:
            db[cat] = [name]

    for key in db.keys():
        answer = answer * (len(db[key]) + 1)
    return answer-1

clothes = [["yellow_hat", "headgear"],
           ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]
solution(clothes)