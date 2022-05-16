arr = []

for i in range(3):
    arr.append(int(input()))

if arr[0] and arr[1] and arr[2] > 0 and sum(arr) == 180:
    if arr[0] == arr[1] == arr[2] == 60:
        print("Equilateral")
        exit()
    elif sum(arr) == 180:
        if arr[0] == arr[1] or arr[0] == arr[2] or arr[1] == arr[2]:
            print("Isosceles")
            exit()
        elif arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2]:
            print("Scalene")
            exit()
else:
    print("Error")
    exit()