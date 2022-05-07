from collections import deque

def solution(que1, que2):

    init1 = sum(que1)
    init2 = sum(que2)

    lens = len(que1)


    target = (init1 + init2) // 2
    que1 = deque(que1)
    que2 = deque(que2)

    flag = True
    answer = 0

    while flag:

        if init1 == init2 == target:
            flag = False

        if answer > lens * 2:
            return -1

        if init1 > target:
            x = que1.popleft()
            que2.append(x)
            init1 -= x
            init2 += x
            answer += 1
            if init1 == init2 == target:
                break

        if init2 > target:
            y = que2.popleft()
            que1.append(y)
            init2 -= y
            init1 += y
            answer += 1
            if init1 == init2 == target:
                break
    #print(answer)
    return answer
que1 = [1, 1]
que2 = [1, 5]


solution(que1, que2)

#
#
#
# from collections import deque
#
# def solution(que1, que2):
#
#     target = (sum(que1) + sum(que2)) // 2
#
#     pop = 0
#     ins = 0
#
#     que1 = deque(que1)
#     que2 = deque(que2)
#
#     flag = True
#
#     while flag:
#         if pop > len(que1) + len(que2) or ins > len(que1) + len(que2):
#             print('here 1 -1')
#             return -1
#
#         if sum(que1) == target and sum(que2) == target:
#             flag = False
#
#         if sum(que1) > target:
#             q1 = que1.popleft()
#             pop += 1
#             que2.append(q1)
#             ins += 1
#
#         if sum(que2) > target:
#             q2 = que2.popleft()
#             pop += 1
#             que1.append(q2)
#             ins += 1
#
#     if pop != ins:
#         print('here 2 -1')
#         return -1
#
#     answer = (pop + ins) // 2
#     print(answer)
#     return answer
# que1 = [1, 2, 1, 1]
# que2 = [2, 1, 1, 1]
# solution(que1, que2)