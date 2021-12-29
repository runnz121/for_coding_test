import heapq
import sys
input = sys.stdin.readline

T = int(input())

q = []

for i in range(T):
    ele = int(input())
    if len(q) > 0:
        if ele == 0:
            print(-heapq.heappop(q))
        else:
            heapq.heappush(q, -ele)
    else:
        if ele == 0:
            print(0)
        else:
            heapq.heappush(q, -ele)

