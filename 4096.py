while True:
    x = str(input())
    count = 0
    if x == '0':
        break

    if x == x[::-1]:
        print(count)
        continue
    else:
        lens = len(x)
        while x != x[::-1]:
            count += 1
            t = int(x) + 1
            x = str(t).zfill(lens)
        print(count)
        continue


