t = int(input())


for i in range(t):
    n = int(input())
    arr = map(int, input().split())
    m = int(input())
    arr1 = map(int, input().split())

    db = dict()
    for k in arr:
        if k not in db:
            db[k] = 1
    for x in arr1:
        if x in db:
            print(1)
        else:
            print(0)