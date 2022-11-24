n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))

    ss = []
    for i in arr:
        if i%2 == 0 and i!= 1:
            ss.append(i)

    print(sum(ss), min(ss))