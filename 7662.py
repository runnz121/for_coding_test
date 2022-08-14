import heapq

T = int(input())

while T > 0:
    k = int(input())

    que = []

    while k > 0:
        st, num = map(str, input().split())

        if st == 'I':
            heapq.heappush(que, int(num))
        elif st == 'D':
            heapq.heappop()



        k -= 1
    print(que)
    T -= 1