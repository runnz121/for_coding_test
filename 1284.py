while True:
    x = int(input())

    if x == 0:
        break

    strings = list(str(x))

    ans = 0
    for i in range(len(strings)):
        if strings[i] == '1':
            ans += 2
        elif strings[i] == '0':
            ans += 4
        else:
            ans += 3
        ans += 1
    print(ans+1)