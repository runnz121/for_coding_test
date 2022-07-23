
while True:
    n = int(input())
    arr = [1 for i in range(n)]
    if n == -1:
        break

    if n == 1 or n == 2:
        cow = 1
    else:
        for k in range(2, len(arr)):
            arr[k] = arr[k-1] + arr[k-2]

        cow = arr[n-1]
    print('Hour %d: %d cow(s) affected' %(n, cow))



