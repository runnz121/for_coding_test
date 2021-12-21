from collections import deque

size, count = map(int, input().split())

target = list(map(int, input().split()))

que = deque()

for i in range(size):
    que.append(i)

#
# target = que[count-1]


#
# cnt = 0
# while True:
#     if que[0] == target:
#         que.popleft()
#         print(cnt)
#         break
#     #왼쪽으로 이동 시키는 경우 -> len/2 했을 때 target이 앞쪽에 있을때
#     if
#
#     #오른쪽은 그 반대