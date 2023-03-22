x = list(str(input().rstrip()))

filtered =[]
for i in x:
    if i.isupper():
        filtered.append(i)

find = ['U','C','P','C']

idx = 0

for i in x:
    if i == find[idx]:
        idx += 1

    if idx == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')