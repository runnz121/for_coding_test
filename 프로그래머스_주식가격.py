from collections import deque

def solution(prices):
    answer = []

    que = deque(prices)
    for i in prices:
        cnt = -1
        for j in range(len(que)):
            res = que.popleft()
            if i <= res:
                cnt += 1
            que.append(res)
        answer.append(cnt)
        que.popleft()

    # print(answer)
    return answer

prices = [1, 2, 3, 2, 3]
solution(prices)