import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

lens = 100001

start = 0
end = 0
sums = 0
while True:
    # 합이 주어진값 보다 크다면
    if sums >= s:
        sums -= arr[start]
        start += 1
        lens = min(lens, end - start + 1)
    else:
        if end == n: # 위에서 start부분이 같이 증가함으로 end 부분만 확인하면 된다
            break
        else:
            sums += arr[end] # 주어진값보다 작다면 end를 하나씩 증가시키면서 전체합 증가
            end += 1

if lens == 100001:
    lens = 0
print(lens)




# while start < n:
#
#     for i in range(start, end+1):
#         sums += arr[i]
#     print(sums, start, end)
#
#     # print(sums,end)
#     if end < n:
#         if sums >= s:
#             if start == end:
#                 case = end-start
#             else:
#                 case = end-start + 1
#
#             lens = min(lens, case)
#             print("correct",sums, lens, start, end)
#             start += 1
#             end = start
#         elif sums < s:
#            # print(sums, end)
#             end += 1
#
#         if end > n:
#             start += 1
#             end = start
#     else:
#         start += 1
#         end = start
#
#     if lens == 1:
#         break
#     sums = 0
#
# if lens == sys.maxsize:
#     print(0)
# else:
#     print(lens)