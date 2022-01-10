import heapq
import sys
cnt = int(input())
q= []
for i in range(cnt):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) > 0:
            res = heapq.heappop(q)
            if res[1] == -1:
                print(res[0] * -1)
            else:
                print(res[0])
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(q,[-x,-1])
        else:
            heapq.heappush(q,[x,1])
