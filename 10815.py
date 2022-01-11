import sys

a = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))

b = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

arr1.sort()

def binary(arr, target, start, end):
    while start<= end:
        mid=(start + end) //2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            end = mid - 1
        else:
            start = mid + 1
    return None
for i in range(b):
    if binary(arr1, arr2[i], 0, a-1) is not None:
        print(1, end=' ')
    else:
        print(0, end = ' ')
