import math

flag = 1

while flag == 1:
    n = int(input())
    if n == 0:
        flag = -1

    arr = [True] * (2*n+1)

    for i in range(2, int(math.sqrt(2*n))+1):
        if arr[i] == True:
            j = 2
            while i * j <= 2*n:
                arr[i * j] = False
                j += 1
    if n == 1:
        print(1)
    elif n == 0:
        print("")
    else:
        print(arr[n+1:].count(True))
