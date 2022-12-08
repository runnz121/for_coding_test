
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        exit()
    db = dict()
    for i in range(n):
        x = int(input())
        db[x] = 1

    sums = 0
    for j in range(m):
        y = int(input())
        if y in db:
            sums += 1
    print(sums)