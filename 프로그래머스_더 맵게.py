import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)


    for i in range(len(scoville)):
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        elif first < K and len(scoville) == 0:
            answer = -1
            return answer
        else:
            second = heapq.heappop(scoville)
            mixed = first + second * 2
            heapq.heappush(scoville, mixed)
            answer += 1

    if len(scoville) == 0:
        answer = -1

    return answer

scoville = [1, 2]
k = 100
solution(scoville, k)