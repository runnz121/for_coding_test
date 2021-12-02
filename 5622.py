sts = str(input())
lens = len(sts)
db = dict()

db['A'] = 2
db['B'] = 2
db['C'] = 2
db['D'] = 3
db['E'] = 3
db['F'] = 3
db['G'] = 4
db['H'] = 4
db['I'] = 4
db['J'] = 5
db['K'] = 5
db['L'] = 5
db['M'] = 6
db['N'] = 6
db['O'] = 6
db['P'] = 7
db['Q'] = 7
db['R'] = 7
db['S'] = 7
db['T'] = 8
db['U'] = 8
db['V'] = 8
db['W'] = 9
db['X'] = 9
db['Y'] = 9
db['Z'] = 9

ans = 0
for i in range(len(sts)):
    ans += db[sts[i]]
ans += lens
print(ans)