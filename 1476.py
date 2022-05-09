e, s, m = map(int, input().split())

for i in range(1, 10000000):
    if (i - e) % 15 == 0:
        if (i - s) % 28 == 0:
            if (i - m) % 19 == 0:
                print(i)
                exit()