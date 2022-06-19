n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

cnt = 0
for i in range(1, n):
    if arr[0] == arr[i]:
        cnt += 1

if cnt + 1 > arr[0]:
    print(arr[0] + 1)
else:
    print(cnt + 1)