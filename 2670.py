
n = int(input())

arr = []
dp = []

for i in range(n):
    x = float(input())
    arr.append(x)

maxx = arr[0]

for i in range(n-1):
    tmp = arr[i]
    for j in range(i+1, n):
        tmp *= arr[j]
        maxx = max(tmp, maxx)

print("%.3f" %(maxx))

# print(arr)
#
# N = int(input())
# nums = [float(input()) for _ in range(N)]
# for i in range(1, N):
#     nums[i] = max(nums[i - 1] * nums[i], nums[i])
#
# print(nums)
# print("{:.3f}".format(max(nums)))