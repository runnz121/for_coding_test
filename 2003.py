a, b = map(int, input().split())

arr = list(map(int, input().split()))

ptr1 = 0
ptr2 = 1
ans = 0

while ptr1 < ptr2 <= a:

    init = arr[ptr1] + arr[ptr2]

    if init == a:
        ans += 1
        ptr1 += 1
        ptr2 += 1
    else:
        ptr2 += 1
        if ptr2 == a:
            if ptr1 == a-1:
                ptr2 -= 1
                ptr1 += 1
print(ans)