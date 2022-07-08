a, b = map(int, input().split())

arr = [i for i in range(a, b + 1)]


db = {'0':'zero', '1':'one', '2':'two', '3':'three','4':'four', '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}

toString = []

ansArr = []

for i in arr:
    x = list(str(i))
    ans = ''

    for i in x:
        ans += db[i] + ' '
    toString.append(ans.rstrip())

toString.sort()
for x in toString:
    temp = ''
    for k in x.split(' '):
        for key, value in db.items():
            if value == k:
                temp += key
    ansArr.append(int(temp))

start = 0
while True:
    if start + 10 > len(ansArr):
        print(*ansArr[start:])
        break
    print(*ansArr[start:start + 10])
    start += 10