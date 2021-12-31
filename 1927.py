import sys
import heapq
input = sys.stdin.readline
t = int(input())
q = []
for i in range(t):
    x = int(input())
    if x == 0:
        if len(q) > 0:
            res = heapq.heappop(q)
            print(res)
        else:
            print(0)
    else:
        heapq.heappush(q, x)

# print(q)