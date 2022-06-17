a, b = map(int, input().split())

arr = list(map(int, input().split()))

ptr1 = 0
ptr2 = 1

cnt = 0

if b >= 2:
    while True:
        sums = arr[ptr1] + arr[ptr2]

        if sums == b:
            cnt += 1
            sums -= arr[ptr1]
            sums += arr[ptr2]
            ptr1 += 1
            ptr2 += 1

        elif sums < b:
            ptr2 += 1
            sums += arr[ptr2]
        else:
            ptr1 += 1
            sums -= arr[ptr1]

        if ptr1 > a-1:
            break

        if ptr2 > a:
            ptr1 += 1
            ptr2 = ptr1 + 1


else:
    if arr[0] != b:
        print(0)
    else:
        print(1)



print(cnt)