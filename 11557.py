n  = int(input())

for i in range(n):
    t = int(input())

    arr = []
    for k in range(t):
        name, a = map(str, input().split())
        arr.append([name, int(a)])

    arr = sorted(arr, key = lambda x : -x[1])
    print(arr[0][0])