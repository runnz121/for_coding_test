# import operator
# import sys
#
# T = int(sys.stdin.readline())
#
# arr = []
# check = dict()
#
# for _ in range(T):
#     arr.append(int(sys.stdin.readline()))
#     check[int(sys.stdin.readline())] += 1
# print(check)
#
# #산술평균
# sum_ele = round(sum(arr)/T)
#
# #중앙값 (sorted -> 새로운 배열 반환)
# arrcp = sorted(arr)
# mid = len(arrcp)//2
# center = arrcp[mid]
#
# #최빈값
# # check = dict()
# # max_value = -1e9
# # for i in arr:
# #     cnt = arr.count(i)
# #     check[i] = cnt
# #
# # # sdict = sorted(check.items(), key = lambda x: (-x[1]))
# #
# sdict = sorted(check.items(), key = lambda x: (-x[1], x[0])) # 최빈값 높은것으로 정렬
# # # print("1", sdict)
# # # #sdict = sorted(check.items(), key = lambda x: (x[0], -x[1]))
# # # print("3", sdict)
# if T == 1:
#      most = sdict[0][0]
# if T >= 2 and sdict[0][1] == sdict[1][1]: # 맨 처음이랑, 두번째 최빈값이 같으면
#     # if sdict[0][0] > sdict[1][0]:
#     #     sdict = sorted(check.items(), key=operator.itemgetter(1))
#     #     print("2", sdict)
#         most = sdict[1][0]
#         #print("most", most)
#
#
#
#
# #범위
# arr.sort()
# ranges = abs(arr[0] - arr[len(arr)-1])
#
#
# sys.stdout.write(str(sum_ele)+'\n')
# sys.stdout.write(str(center)+'\n')
# sys.stdout.write(str(most)+'\n')
# sys.stdout.write(str(ranges)+'\n')
#

import sys

T = int(input())

arr = []
check = dict()

for i in range(T):
    arr.append(int(sys.stdin.readline()))
# 산술평균
print(round(sum(arr)/T))
# 중앙값
arr.sort()
print(arr[len(arr)//2])
# 최빈값

p = -4001
count = 0  # 현재 숫자가 등장한 횟수
best = 1  # 최빈값의 등장 횟수
mode = []  # 최빈값 목록

# 이미정렬되어 있기 때문에 앞에서부터 하나씩 등장하면 그냥 1만 더해주어서
for i in arr:
    if i == p:
        count += 1
    else:
        count = 1

    if count == best:
        mode.append(i)
    elif count > best:
        mode = [i]
        best = count # 최빈값 갱신
    p = i # 다음 인덱스로 넘어감

try:
    print(mode[1])
except:
    print(mode[0])

print(abs(min(arr) - max(arr)))