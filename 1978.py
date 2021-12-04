n =int(input())
arr = list(map(int, input().split()))

count = 0
check= []

for i in range(n):
    for j in range(1, arr[i]+1):
        res = arr[i] % j
        if res == 0:
            check.append(j)
    if 2 <= len(check) < 3:
        count += 1
    check = []
print(count)