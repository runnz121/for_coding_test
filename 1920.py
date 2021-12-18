T1 = int(input())
arr1 = list(map(int, input().split()))
T2 = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()



def binary(target):
    left = 0
    right = T1 - 1

    while left <= right:
        mid = (left+right)//2
        if arr1[mid] == target:
            print(arr1[mid], mid, target)
            return True

        if target < arr1[mid]:
            right = mid - 1
        elif target > arr1[mid]:
            left = mid + 1

for i in range(T2):
    if binary(arr2[i]):
        print(1)
    else:
        print(0)
