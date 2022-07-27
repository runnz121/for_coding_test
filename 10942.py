n = int(input())

arr = list(map(int, input().split()))

m = int(input())

while m > 0:
    s, e = map(int, input().split())
    s = s-1
    print(arr[s:e])

    if len(arr[s:e]) == 2 or len(arr[s:e]) % 2 == 0:
        print(0)

    else:
        while True:
            find = arr[s:e]
            if s == e - 1:
                break
            if find[s] != find[e-1]:
                break


            s += 1
            e -= 1

    m -= 1



# 1 2 3 2 1 2 3 5