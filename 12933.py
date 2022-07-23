string = list((input()))
ans = 0


db = {'q':0,'u':0,'a':0,'c':0,'k':0}

flag= True

for i in range(len(string)):
    if string[i] == 'q':
        db['q'] += 1
    elif string[i] == 'u':
        db['u'] += 1
        if db['q'] < db['u']:
            flag = False
            break
    elif string[i] == 'a':
        db['a'] += 1
        if db['u'] < db['a']:
            flag = False
            break
    elif string[i] == 'c':
        db['c'] += 1
        if db['a'] < db['c']:
            flag = False
            break
    elif string[i] == 'k':
        db['k'] += 1
        if db['c'] < db['k']:
            flag = False
            break


if db['q'] == db['u'] == db['a'] == db['c'] == db['k']:
    flag = True
else:
    flag = False


if flag == True:

    ss = list(filter(lambda x: x == 'k' or x == 'q', string))

    qkonly = ''.join(ss)

    for x in qkonly:
        if x == 'q':
            ans += 1

    sss = qkonly.replace('kq', 'x')

    for p in sss:
        if p == 'x':
            ans -= 1

    print(ans if ans else -1)
else:
    print(-1)
    exit()