# import sys
#
# T = int(input())
# arr = []
#
# # https://apnalchangx2.tistory.com/12
#
# for i in range(T):
#     arr.append(int(sys.stdin.readline()))
#
# def quicksort(arr):
#     if len(arr) <= 1: # 리스트가 1이면 정렬할 필요 없음
#         return arr
#     pivot = arr[len(arr)//2]  # 리스트에서 원하는 피벗 선택
#     left = []    # 피벗보다 작은 리스트
#     right = []  # 피벗보다 큰 리스트
#     piv = []    # 피벗 빼놓고 나눠야 하니깐 피벗 넣을 리스트
#
#     for i in arr:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             piv.append(i)
#
#     return quicksort(left) + piv + quicksort(right) # 재귀로 돌림(
# arr = quicksort(arr)
#
# for k in arr:
#     print(k)


#파이썬 기본 정렬 함수가 이미잘 구성되어있음( nlog(n))
import sys

n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i) + '\n')

# 1 3 2 5 6 7 4
# pivot = 5, left = 1 3 2 4, right = 6 7 -> 아래서 반환값이( 1 2 3 4 + 5 + 6 7)

# left
# pivot = 2 left = 1, right = 3 4 -> 1 + 2 + 3 4
# right
# pivot = 3 left =  right = 4 -> 3 + 4

# right
# pivot = 7 left = 6, right =  -> 6 + 7