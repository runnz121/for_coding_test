x = int(input())

db = dict()

for i in range(x):
    strs = str(input())
    if strs in db:
        db[strs] += 1
    else:
        db[strs] = 1

res = sorted(db.items(), key = lambda x : (-x[1], x[0]) )

print(res[0][0])