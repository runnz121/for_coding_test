def soluton(tstring, variables):

    def union(db, x):
        try:
            if db[x].startswith('{'):
                union(db, db[x])
        except KeyError:
            return db[x]
        return db[x]

    db = dict()

    for i in variables:
        db[i[0]] = i[1]

    print("1", db)

    for key in db.keys():
        if db[key].startswith('{'):
            x = db[key][1:-1]
            db[key] = union(db, x)


    print("2", db)

    list_tstring = tstring.split(" ")

    for k in range(len(list_tstring)):
        if list_tstring[k].startswith('{'):
            find = list_tstring[k][1:-1]

            res = union(db, find)

            list_tstring[k] = res



    print(list_tstring)
    answer = " ".join(list_tstring)
    print(answer)

    return answer


tstring = "this is {template} {template} is {state}"
variables = [["template", "{state}"], ["state", "{template}"]]
soluton(tstring, variables)
