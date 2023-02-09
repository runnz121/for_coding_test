n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

for i in range(n):
    arr[i] = arr[i] + i + 1

print(max(arr) +1)