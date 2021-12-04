n = int(input())

if n == 1:
    print()
arr = []
i = 2
while n > 1:
    if n % i == 0:
        n = n // i
        arr.append(i)
        i = 2
    else:
        i += 1

arr.sort()
for i in range(len(arr)):
    print(arr[i])