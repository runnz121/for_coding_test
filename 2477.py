n = int(input())

x = []
y = []

db = dict()

for i in range(6):
    d, cm = map(int, input().split())

    if d == 1 or d == 2:
        x.append(cm)
    else:
        y.append(cm)

    if d not in db:
        db[d] = [cm]
    else:
        db[d].append(cm)

minus = []

db = sorted(db.items(), key = lambda x : (x[1]))
for i in db:
    if len(i[1]) >= 2:
        minus.append(min(i[1]))

#
# print(x)
# print(y)

mn = minus[0] * minus[1]
total = max(x) * max(y)
# print(total, mn)

print((total - mn) * n )
