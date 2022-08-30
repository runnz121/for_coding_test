while True:
    try:
        n = int(input())
    except:
        break

    i = ''
    while True:
        i += '1'
        i = int(i)

        if i%2 != 0 and i%5 != 0 and i%n == 0:
            print(len(str(i)))
            break
        i = str(i)