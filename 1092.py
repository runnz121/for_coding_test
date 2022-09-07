n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort(reverse=True)
arr2.sort(reverse=True)

# 짐 무게 기준
check = [False] * m

# 무게 최대값이 크레인최대 허용중량보다 크면
if max(arr1) < max(arr2):
    print(-1)
    exit()

print(arr2)
# 크레인 갯수만큼 자름
start = -n
for i in range(0, m, n):
    if i == 0:
        x = arr2[:n]
    else:
        x = arr2[i:i * 2]


# print(arr1)
# print(arr2)