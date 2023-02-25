n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))

    db = dict()

    f = arr[0]
    lists = arr[1:]

    for i in lists:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1

    db = sorted(db.items(), key = lambda x : x[1], reverse=True)

    if len(db) >= 2 and db[0][1] == db[1][1]:
        print("SYJKGW")
    else:
        print(db[0][0])