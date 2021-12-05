while True:
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0]==0 and arr[1]==0 and arr[2] == 0:
        break
    if arr[2] <= arr[0] + arr[1] and arr[2]**2 == arr[0]**2 + arr[1]**2:
        print("right")
    else:
        print("wrong")
