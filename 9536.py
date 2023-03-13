n = int(input())

for i in range(n):
    howl = list(map(str, input().split()))

    while True:
        case = list(map(str, input().split()))

        if case[0] == 'what':
            res = ''
            for i in range(len(howl)):
                if howl[i] != '':
                    if i != len(howl) - 2:
                        res += howl[i] + ' '
                    else:
                        res += howl[i]

            print(res)
            break

        for i in range(len(howl)):
            if case[2] == howl[i]:
                howl[i] = ''
