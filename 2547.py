n = int(input())

for i in range(n):
    x = input()

    k = int(input())
    arr = []
    for p in range(k):
        a = int(input())
        arr.append(a)

    if sum(arr) % k == 0:
        print("YES")
    else:
        print("NO")