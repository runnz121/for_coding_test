#
# import sys
# T = int(input())
#
# arr = []
#
# for i in range(T):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
#
# arr = sorted(arr, key = lambda x: (x[0], x[1]))
# max_end = max(arr)
# max_value = -1e9
# print(arr)
#
# for i in range(T):
#     count = 1
#     start = arr[i][0]
#     end = arr[i][1]
#
#     for j in range(i, T):
#         if arr[j][0] >= end:
#             # print(arr[j])
#             count += 1
#             end = arr[j][1]
#     max_value = max(count, max_value)
#
# print(max_value)

import sys
T = int(input())
arr = []
check = []
for i in range(T):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr = sorted(arr, key = lambda x: (x[1], x[0])) # 종료 시간 기준먼저 정렬 후 시작시간 정렬
#
# arr = sorted(arr, key = lambda x: x[0])
# arr = sorted(arr, key = lambda x : x[1])
# print(arr)
count = 0 # 회의 갯수 새기
end = 0 # 마지막 시간

for i, j in arr:
    if i >= end:
        count += 1
        end = j
print(count)


# end = arr[0][1]
# for i in range(T):
#     if arr[i][0] >= end:
#         end = check[i][0]
#         count += 1
# print(count)