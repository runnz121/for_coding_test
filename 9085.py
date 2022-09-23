n = int(input())

for i in range(n):
    x = int(input())
    arr = list(map(int, input().split()))

    print(sum(arr))