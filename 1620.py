n, m = map(int, input().split())

db = dict()
ans = []

idx = 1
for i in range(0, n):
    pokemon = str(input())
    db[pokemon] = idx
    idx += 1

lis = list(db)

for k in range(m):
    find = input()
    if find.isnumeric():
        print(lis[int(find)-1])
    else:
        print(db[str(find)])