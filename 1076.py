a = str(input())
b = str(input())
c = str(input())


db = dict()

db['black'] = [0,1]
db['brown'] = [1,10]
db['red'] = [2,100]
db['orange'] = [3,1000]
db['yellow'] = [4,10000]
db['green'] = [5,100000]
db['blue'] = [6,1000000]
db['violet'] = [7,10000000]
db['grey'] = [8,100000000]
db['white'] = [9,1000000000]

aa = db[a][0]
bb = db[b][0]
cc = db[c][1]

print((aa * 10 + bb) * cc)
