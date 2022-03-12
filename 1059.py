a = int(input())

arr = list(map(int, input().split()))

b = int(input())


answer = 0

if b in arr:
    answer = 0

else:
    for i in range(a):
        for j in range(i, a):
            if