n = int(input())
for i in range(n):

    cnt = 0
    call = 1
    ispal = 0
    x = str(input())

    x = list(x)
    start = 0
    lens = len(x)-1

    def recurs(x, start, lens):

        global ispal
        global call

        if start >= lens:
            ispal = 1
            return
        elif x[start] != x[lens]:
            ispal = 0
        else:
            call += 1
            recurs(x, start + 1, lens - 1)

    recurs(x, start, lens)

    print(ispal, call)