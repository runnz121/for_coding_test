from collections import deque
def solution(priorities, location):

    answer = 0
    que = deque([(v, i) for i, v in enumerate(priorities)])

    while len(que):
        item = que.popleft()
        if que and max(que)[0] > item[0]:
            que.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [2, 1, 3, 2]
priorities1 = [1, 1, 9, 1, 1, 1]
location = 2
location1 = 5

solution(priorities, location)