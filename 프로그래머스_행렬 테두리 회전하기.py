import copy
from collections import deque

def solution(rows, columns, queries):
    answer = []

    board = [[]*columns for _ in range(rows)]
    each = []
    idx = []
    check = deque()

    for i in range(1, rows * columns+1):
        each.append(i)
    for j in range(0, len(each) - 1, columns):
        idx.append(j)

    for i in range(rows):
        board[i] = each[idx[i]:idx[i] + columns]



    # print(board)

    for i in range(len(queries)):
        x1 = queries[i][0] -1
        y1 = queries[i][1] -1
        x2 = queries[i][2] -1
        y2 = queries[i][3] -1
        # print(x1, y1, x2, y2)
        #row가 같을때 1
        for a in range(x1, x1 + abs(x1-x2)):
            check.append(board[y1][a])
            print('1',check)
        #column이 같을때 1
        for b in range(y1, y1 + abs(y1-y2)+1):
            check.append(board[b][x2-1])
            print('2', check)
        #row가 같을때 2
        for c in range(x2, abs(x1-x2)-1, -1):
            check.append(board[y2+1][c])
            print('3', check)
        #colum 같을때 2
        for d in range(y1 + abs(y1-y2), y1, -1):
            check.append(board[d][x1])
            print('4', check)
        check.appendleft(check.pop())


        #check 큐에서 꺼내서 재배열
        answer.append(min(check))
        for a in range(x1, x1 + abs(x1 - x2)):
            board[y1][a] = check.popleft()

        for b in range(y1+1, y1 + abs(y1-y2)+1):
            board[b][x2-1] = check.popleft()

        # print('1', check)
        for d in range(y1 + abs(y1-y2)+1, y1, -1):
            board[y2+1][d-1] = check.popleft()
        # print('1', board)

        # print('2', check)
        for d in range(y1 + abs(y1-y2), y1, -1):
            board[d][x1] = check.popleft()
        # print('2',board)
    print(answer)
    return answer
rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
sample = [[2,2,5,4]]
solution(rows, columns, sample)

#     check.append(board[y1][x1:x2])
#     check.append(board[y2+1][x1:x2])
# arr_a= []
# for a in range(y1, y1+abs(y1-y2)+1):
#     arr_a.append(board[a][x2-1])
# check.append(arr_a)
#
# arr_b = []
# for b in range(y2+1, y2 - abs(y1-y2),-1):
#     arr_b.append(board[b][x1])
# check.append(arr_b)
#
# print(check)