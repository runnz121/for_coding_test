n = int(input())
x = list(str(input()))

db = dict()

db['A'] = 0
db['B'] = 0

for i in x:
    if i in db:
        db[i] += 1
    else:
        db[i] = 1

if db['A'] == db['B']:
    print('Tie')
elif db['A'] > db['B']:
    print('A')
else:
    print('B')