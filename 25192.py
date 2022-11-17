n = int(input())

db = dict()

cnt = 0
idx = 0
while True:
    if idx < n:
        x = str(input())
    if x == 'ENTER' or idx == n:
        for key in db:
            cnt += db[key]
        db = dict()
        if idx == n:
            break

    if x != 'ENTER' and x not in db:
        db[x] = 1

    idx += 1
print(cnt)