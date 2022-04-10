from collections import deque

def solution(path):
    answer = []

    turn = ['left','right']

    total = 0
    cnt = 0

    for i in range(1, len(path)):
        flag = path[i-1]
        if path[i] == path[i - 1]:
            cnt += 1
            total += 1

        else:
            x = total - cnt
            y = (cnt + 1) * 100
            cnt = 0
            total += 1

            if flag == 'E' and path[i] == 'S' or flag == 'S' and path[i] == 'W' or flag == 'W' and path[i] == 'N' or flag == 'N' and path[i] == 'E':
                direction = turn[1]
            else:
                direction = turn[0]

            if y > 500:
                x = x + y//100 - 5
                y = 500

            ans = 'Time ' + str(x) + ':' + ' Go straight ' + str(y)+'m' + ' and turn ' + direction
            answer.append(ans)

    print(answer)
    return answer


path = "EEEEEESEEEEEEENNNN"
solution(path)
