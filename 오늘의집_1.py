from collections import deque

def solution(path):
    answer = []
    dir = {'E':0, 'S':0, 'W':0, 'N':0}
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    turn = ['left','right']
    # print(f"Time {x}: Go straight {y}m and turn {direction}")

    q = deque(path)
    total = 0
    cnt = 0
    direction = ''
    ans = ''

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
            #print(x, y, direction)


    print(answer)
    return answer


path = "EEESEEEEEEENNNN"
solution(path)
