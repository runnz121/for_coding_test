# import sys
#
# a = int(input())
# sang = list(map(int, sys.stdin.readline().split()))
#
# b = int(input())
# num = list(map(int, sys.stdin.readline().split()))
#
# ans = []
#
# sang.sort()
#
# def csup(index, target):
#     cnt = 0
#     if sang[index] == target:
#         for i in range(index, len(sang)):
#             if sang[i] == target:
#                 cnt += 1
#             else:
#                 return cnt
#     return cnt
#
# def csdown(index, target):
#     cnt = 0
#     if sang[index-1] == target:
#         for i in range(index-1, -1, -1):
#             if sang[i] == target:
#                 cnt += 1
#             else:
#                 return cnt
#     return cnt
#
# def binary(target):
#     start = 0
#     end = a - 1
#     while start <= end:
#         mid = (start + end)//2
#         if target == sang[mid]:
#             return mid
#         elif target > sang[mid]:
#             start = mid + 1
#         elif target < sang[mid]:
#             end = mid - 1
#         else:
#             return 0
# #
# #print(sang)
# for target in num:
#    res = binary(target)
#    if res != None:
#        cntup = csup(res, target)
#        cntdown = csdown(res, target)
#        cnts = cntup + cntdown
#        # print(res,target)
#        ans.append(cnts)
#    else:
#        ans.append(0)
#
# print(*ans)



n = int(input())
cards = list(map(int, input().split(' ')))
cards.sort()

m = int(input())
targets = list(map(int, input().split(' ')))

dic = dict()

#딕셔너리른 O(1)임으로 이미 있으면 +1 해준다.
for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if targets[i] in dic:
        print(dic[targets[i]], end=' ')
    else:
        print(0, end=' ')