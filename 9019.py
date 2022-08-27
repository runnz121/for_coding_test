# from collections import deque
# # import sys
# # input = sys.stdin.readline
#
# n = int(input())
#
# def bfs(start, end):
#
#     que = deque()
#     que.append([start, ''])
#     check[start] = True
#
#     while que:
#
#         x = que.popleft()
#
#         if x[0] == end:
#             print(x[1])
#             return
#
#         # D
#         dd = x[0] * 2
#         if dd > 9999:
#             dd = dd%10000
#             if not check[dd]:
#                 d = x[1] + 'D'
#                 que.append([dd, d])
#                 check[dd] = True
#
#         # S
#         ss = x[0] - 1
#         if ss == -1:
#             ss = 9999
#         if not check[ss]:
#             s = x[1] + 'S'
#             que.append([ss, s])
#             check[ss] = True
#
#         # L
#         ll = (10 * x[0] + (x[0] // 1000)) % 10000
#         if not check[ll]:
#             l = x[1] + 'L'
#             que.append([ll, l])
#             check[ll] = True
#
#         # R
#         rr = (x[0]//10 + (x[0]%10)*1000)%10000
#         if not check[rr]:
#             r = x[1] + 'R'
#             que.append([rr, r])
#             check[rr] = True
#
#
#
#
#         # # L
#         # ll = list(str(x[0]))
#         # ll = deque(ll)
#         # if len(ll) != 4:
#         #     while len(ll) < 4:
#         #         ll.append('0')
#         # ll.rotate(-1)
#         # ll = int(''.join(ll))
#         # if not check[ll]:
#         #     l = x[1] + 'L'
#         #     que.append([ll, l])
#         #     check[ll] = True
#         #
#         # # R
#         # rr = list(str(x[0]))
#         # rr = deque(rr)
#         # if len(rr) != 4:
#         #     while len(rr) < 4:
#         #         rr.append('0')
#         # rr.rotate(1)
#         # rr = int(''.join(rr))
#         # if not check[rr]:
#         #     r = x[1] + 'R'
#         #     que.append([rr, r])
#         #     check[rr] = True
#
#
# for i in range(n):
#     x, y = map(int, input().split())
#     check = [False] * 10001
#     bfs(x, y)

from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque()
    q.append((A, ""))
    visit = [False] * 10000

    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        # 1
        num2 = (2 * num) % 10000
        if not visit[num2]:
            q.append((num2, path + "D"))
            visit[num2] = True
        # 2
        num2 = (num - 1) % 10000
        if not visit[num2]:
            q.append((num2, path + "S"))
            visit[num2] = True
        # 3
        num2 = (10 * num + (num // 1000)) % 10000
        if not visit[num2]:
            q.append((num2, path + "L"))
            visit[num2] = True

        # 4
        num2 = (num // 10 + (num % 10) * 1000) % 10000
        if not visit[num2]:
            q.append((num2, path + "R"))
            visit[num2] = True


