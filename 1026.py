T = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_cp = sorted(arr1)
arr2_cp = sorted(arr2, reverse=True)

sss = 0
for i in range(T):
    sss += arr1_cp[i] * arr2_cp[i]

print(sss)