n = int(input())
m = int(input())

arr1 = [[0]*n for _ in range(n)]
arr2 = []

for i in range(n):
    for j in range(n):
        arr1[i][j] = (i+1) * (j+1)
        arr2.append((arr1[i][j]))

arr2.sort()
#
# start, end = 0, max(arr2)
# while start <= end:
#     mid = (start + end)//2

# print(arr1)
print(arr2[m])

