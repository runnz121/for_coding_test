import copy


def soluton(tstring, variables):

    answer = ''

    db = dict()

    def dfs(db, x, first):
        if first == db[x]:
            return first

        if db[x].startswith('{') and db[x][1:-1] in db: # {e}
            return dfs(db, db[x][1:-1], first) # db, e, {d}
        return db[x]

    for i in variables:
        db[i[0]] = i[1]

    list_tstring = tstring.split(" ")

    for i in range(len(list_tstring)):
        find = list_tstring[i]
        if find.startswith('{') and find[1:-1] in db:
            change = dfs(db, find[1:-1], find) # db, d, {d}
            print(change)
            list_tstring[i] = change



    answer = ' '.join(list_tstring)
    print(answer)
    return answer


tstring = "{a} {b} {c} {d} {i}"
variables = [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]

soluton(tstring, variables)
