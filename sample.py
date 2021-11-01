import heapq

heap = [10,4,304,20,40,60,4,5,6,67,90]

heapq.heapify(heap)

for i in range(len(heap)):
   res = heapq.heappop(heap)
   print(res)
