
import heapq
import sys

t = int(sys.stdin.readline())

# 최대힙, 최소힙 2개를 선언
# 최대힙의 첫번째 요소는 항상 중앙값이다
mx_q , mi_q = [] , []

for i in range(t):
    num = int(sys.stdin.readline())

    if len(mx_q) == len(mi_q):
        heapq.heappush(mx_q, -num)
    else:
        heapq.heappush(mi_q, num)

    if len(mx_q) >= 1 and len(mi_q)>=1 and mx_q[0] * -1 > mi_q[0]:
        max_val = heapq.heappop(mx_q) * -1
        min_val = heapq.heappop(mi_q)

        heapq.heappush(mx_q, min_val * -1)
        heapq.heappush(mi_q, max_val)
    print(mx_q[0] * -1)



# for i in range(1, t+1):
#     heapq.heappush(q, int(sys.stdin.readline()))
#     q_copy = q[::]
#
#     if i % 2 == 0:
#         for _ in range(i//2-1):
#             heapq.heappop(q)
#         print(heapq.heappop(q))
#     else:
#         for _ in range(i//2):
#             heapq.heappop(q)
#         print(heapq.heappop(q))
#     q = q_copy

