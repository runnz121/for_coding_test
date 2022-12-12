while True:
    x, n, m = map(str, input().split())

    if x == '#' and int(n) == 0 and int(m) == 0:
        break

    if int(n) > 17 or int(m) >= 80:
        print(x + ' ' + 'Senior')
    else:
        print(x + ' ' + 'Junior')
