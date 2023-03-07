n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    idx = 0
    count = 0
    a.sort()
    b.sort()

    for i in range(x):
        while True:
            if idx == y or a[i] <= b[idx]:
                count += idx
                break
            else:
                idx += 1
    print(count)