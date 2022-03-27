import heapq

def solution(A, B):
    answer = 0

    a = []
    b = []

    for i in range(len(A)):
        heapq.heappush(a, -A[i])

    for j in range(len(B)):
        heapq.heappush(b, -B[j])


    for k in range(len(A)):
        aa = -heapq.heappop(a)
        bb = -heapq.heappop(b)

        if bb > aa:
            answer += 1


    print(answer)
    return answer

A = [5,1,3,7]
B = [2,2,6,8]
solution(A, B)