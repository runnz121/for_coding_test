import math
T = int(input())

while T > 0:
    arr = list(map(int, input().split()))

    x = (arr[0] - arr[3])**2
    y = (arr[1] - arr[4])**2
    mid = math.sqrt(x+y)

    r1 = arr[2]
    r2 = arr[5]

    if mid == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if r1 + r2 == mid or abs(r2 - r1) == mid:
            print(1)
        elif (abs(r1-r2) < mid) and (mid < r1 + r2):
            print(2)
        else:
            print(0)
    T -=1

