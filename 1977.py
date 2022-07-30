x = int(input())
y = int(input())

arr = []

start = 1
while True:
    if (start ** 2) > y:
        break

    else:
        if x <= start ** 2 <= y:
            arr.append(start**2)
    start += 1

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])