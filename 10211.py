n = int(input())

for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))

    check = [0] * m
    check[0] = arr[0]

    for i in range(1, m):
        check[i] = max(check[i-1] + arr[i], arr[i])

    print(max(check))