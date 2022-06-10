arr =list(map(int, input().split()))

if arr[0] < arr[1]:

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            print('mixed')
            break
    else:
        print('ascending')

elif arr[1] < arr[0]:
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            print('mixed')
            exit()
    print('descending')